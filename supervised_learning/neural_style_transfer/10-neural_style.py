#!/usr/bin/env python3
import numpy as np
import tensorflow as tf

class NST:
    def __init__(self, style_image, content_image, alpha=1e4, beta=1, var=10):
        if not isinstance(style_image, np.ndarray) or style_image.shape[-1] != 3:
            raise TypeError("style_image must be a numpy.ndarray with shape (h, w, 3)")
        if not isinstance(content_image, np.ndarray) or content_image.shape[-1] != 3:
            raise TypeError("content_image must be a numpy.ndarray with shape (h, w, 3)")
        if not isinstance(alpha, (int, float)) or alpha < 0:
            raise TypeError("alpha must be a non-negative number")
        if not isinstance(beta, (int, float)) or beta < 0:
            raise TypeError("beta must be a non-negative number")
        if not isinstance(var, (int, float)) or var < 0:
            raise TypeError("var must be a non-negative number")

        self.alpha = alpha
        self.beta = beta
        self.var = var

        tf.config.run_functions_eagerly(True)
        self.style_image = self.preprocess_image(style_image)
        self.content_image = self.preprocess_image(content_image)

        self.model = self.load_model()
        self.gram_style_features = self.get_style_features(self.style_image)
        self.content_feature = self.get_content_feature(self.content_image)

    @staticmethod
    def preprocess_image(image):
        image = tf.convert_to_tensor(image, dtype=tf.float32)
        image = tf.image.resize(image, (224, 224))
        image = tf.keras.applications.vgg19.preprocess_input(image)
        image = tf.expand_dims(image, axis=0)
        return image

    def load_model(self):
        vgg = tf.keras.applications.VGG19(include_top=False, weights='imagenet')
        vgg.trainable = False
        style_layers = ['block1_conv1', 'block2_conv1', 'block3_conv1', 'block4_conv1', 'block5_conv1']
        content_layers = ['block5_conv2']
        selected_layers = style_layers + content_layers
        outputs = [vgg.get_layer(name).output for name in selected_layers]
        model = tf.keras.Model([vgg.input], outputs)
        return model

    def gram_matrix(self, input_tensor):
        channels = int(input_tensor.shape[-1])
        a = tf.reshape(input_tensor, [-1, channels])
        n = tf.shape(a)[0]
        gram = tf.matmul(a, a, transpose_a=True)
        return gram / tf.cast(n, tf.float32)

    def get_style_features(self, style_image):
        outputs = self.model(style_image)
        style_outputs = outputs[:5]
        return [self.gram_matrix(style_output) for style_output in style_outputs]

    def get_content_feature(self, content_image):
        outputs = self.model(content_image)
        return outputs[-1]

    @staticmethod
    def variational_cost(generated_image):
        x_deltas = generated_image[:, 1:, :, :] - generated_image[:, :-1, :, :]
        y_deltas = generated_image[:, :, 1:, :] - generated_image[:, :, :-1, :]
        var_cost = tf.reduce_sum(tf.abs(x_deltas)) + tf.reduce_sum(tf.abs(y_deltas))
        print("Variational Cost:", var_cost)  # Debugging line
        return var_cost

    def total_cost(self, generated_image):
        generated_outputs = self.model(generated_image)
        generated_style_outputs = generated_outputs[:5]
        generated_content_output = generated_outputs[-1]

        J_content = self.alpha * tf.reduce_mean(tf.square(generated_content_output - self.content_feature))
        print("Content Cost:", J_content)  # Debugging line

        J_style = 0
        for gram_style, generated_style in zip(self.gram_style_features, generated_style_outputs):
            gram_generated_style = self.gram_matrix(generated_style)
            J_style += tf.reduce_mean(tf.square(gram_generated_style - gram_style))
        J_style *= self.beta
        print("Style Cost:", J_style)  # Debugging line

        J_var = self.var * self.variational_cost(generated_image)
        print("Total Variational Cost:", J_var)  # Debugging line

        J_total = J_content + J_style + J_var
        print("Total Cost:", J_total)  # Debugging line

        return J_total, J_content, J_style, J_var

    def generate_image(self, iterations=1000, step=None, lr=0.01, beta1=0.9, beta2=0.99):
        if not isinstance(iterations, int):
            raise TypeError("iterations must be an integer")
        if iterations <= 0:
            raise ValueError("iterations must be positive")
        if step is not None and not isinstance(step, int):
            raise TypeError("step must be an integer")
        if step is not None and (step <= 0 or step >= iterations):
            raise ValueError("step must be positive and less than iterations")
        if not isinstance(lr, (float, int)):
            raise TypeError("lr must be a number")
        if lr <= 0:
            raise ValueError("lr must be positive")
        if not isinstance(beta1, float):
            raise TypeError("beta1 must be a float")
        if not 0 <= beta1 <= 1:
            raise ValueError("beta1 must be in the range [0, 1]")
        if not isinstance(beta2, float):
            raise TypeError("beta2 must be a float")
        if not 0 <= beta2 <= 1:
            raise ValueError("beta2 must be in the range [0, 1]")

        generated_image = tf.Variable(self.content_image, dtype=tf.float32)
        optimizer = tf.optimizers.Adam(learning_rate=lr, beta_1=beta1, beta_2=beta2)
        best_cost = float('inf')
        best_image = None

        for i in range(iterations):
            with tf.GradientTape() as tape:
                J_total, J_content, J_style, J_var = self.total_cost(generated_image)
            grads = tape.gradient(J_total, generated_image)
            optimizer.apply_gradients([(grads, generated_image)])

            if J_total < best_cost:
                best_cost = J_total
                best_image = generated_image.numpy()

            if step is not None and i % step == 0:
                print(f"Cost at iteration {i}: {J_total}, content {J_content}, style {J_style}, var {J_var}")

        return best_image, best_cost
