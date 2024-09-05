#!/usr/bin/env python3
"""
Defines class NST that performs tasks for neural style transfer
"""


import numpy as np
import tensorflow as tf


class NST:
    """
    Performs tasks for Neural Style Transfer

    public class attributes:
        style_layers = ['block1_conv1', 'block2_conv1', 'block3_conv1',
                        'block4_conv1', 'block5_conv1']
        content_layer = 'block5_conv2'

    instance attributes:
        style_image: preprocessed style image
        content_image: preprocessed style image
        alpha: weight for content cost
        beta: weight for style cost

    class constructor:
        def __init__(self, style_image, content_image, alpha=1e4, beta=1)

    static methods:
        def scale_image(image):
            rescales an image so the pixel values are between 0 and 1
                and the largest side is 512 pixels
    """
    style_layers = ['block1_conv1', 'block2_conv1', 'block3_conv1',
                    'block4_conv1', 'block5_conv1']
    content_layer = 'block5_conv2'

    def __init__(self, style_image, content_image, alpha=1e4, beta=1):
        """
        Class constructor for Neural Style Transfer class

        parameters:
            style_image [numpy.ndarray with shape (h, w, 3)]:
                image used as style reference
            content_image [numpy.ndarray with shape (h, w, 3)]:
                image used as content reference
            alpha [float]: weight for content cost
            beta [float]: weight for style cost
        """
        if type(style_image) is not np.ndarray or len(style_image.shape) != 3:
            raise TypeError("style_image must be a numpy.ndarray with shape (h, w, 3)")
        if type(content_image) is not np.ndarray or len(content_image.shape) != 3:
            raise TypeError("content_image must be a numpy.ndarray with shape (h, w, 3)")
        
        if (type(alpha) is not float and type(alpha) is not int) or alpha < 0:
            raise TypeError("alpha must be a non-negative number")
        if (type(beta) is not float and type(beta) is not int) or beta < 0:
            raise TypeError("beta must be a non-negative number")

        self.style_image = self.scale_image(style_image)
        self.content_image = self.scale_image(content_image)
        self.alpha = alpha
        self.beta = beta

        self.load_model()
        self.generate_features()

    @staticmethod
    def scale_image(image):
        """
        Rescales an image such that its pixel values are between 0 and 1
            and its largest side is 512 pixels
        """
        h, w, c = image.shape
        if h > w:
            h_new = 512
            w_new = int(w * (512 / h))
        else:
            w_new = 512
            h_new = int(h * (512 / w))

        resized = tf.image.resize(np.expand_dims(image, axis=0), size=(h_new, w_new))
        rescaled = resized / 255.0
        return tf.clip_by_value(rescaled, 0, 1)

    def load_model(self):
        """
        Loads the VGG19 model, keeping only the specified layers for style
        and content extraction.
        """
        vgg = tf.keras.applications.VGG19(include_top=False, weights='imagenet')
        vgg.trainable = False

        style_outputs = [vgg.get_layer(name).output for name in self.style_layers]
        content_output = vgg.get_layer(self.content_layer).output

        model_outputs = style_outputs + [content_output]

        self.model = tf.keras.Model(vgg.input, model_outputs)

    @staticmethod
    def gram_matrix(input_layer):
        """
        Calculates the Gram matrix of an input tensor.
        """
        result = tf.linalg.einsum('bijc,bijd->bcd', input_layer, input_layer)
        input_shape = tf.shape(input_layer)
        num_locations = tf.cast(input_shape[1] * input_shape[2], tf.float32)
        return result / num_locations

    def generate_features(self):
        """
        Extracts the style and content features from the pre-trained VGG19 model.
        """
        vgg19_model = tf.keras.applications.vgg19

        preprocess_style = vgg19_model.preprocess_input(self.style_image * 255)
        preprocess_content = vgg19_model.preprocess_input(self.content_image * 255)

        style_features = self.model(preprocess_style)[:-1]
        content_feature = self.model(preprocess_content)[-1]

        gram_style_features = [self.gram_matrix(feature) for feature in style_features]

        self.gram_style_features = gram_style_features
        self.content_feature = content_feature

    def layer_style_cost(self, style_output, gram_target):
        """
        Calculates the style cost for a single layer.
        """
        gram_style = self.gram_matrix(style_output)
        return tf.reduce_mean(tf.square(gram_style - gram_target))

    def style_cost(self, style_outputs):
        """
        Calculates the overall style cost from all style layers.
        """
        style_cost = 0
        weight = 1 / len(self.style_layers)

        for i in range(len(style_outputs)):
            style_cost += weight * self.layer_style_cost(style_outputs[i], self.gram_style_features[i])

        return style_cost

    def content_cost(self, content_output):
        """
        Calculates the content cost.
        """
        return tf.reduce_mean(tf.square(content_output - self.content_feature))

    def total_cost(self, generated_image):
        """
        Calculates the total cost: a weighted sum of content and style cost.
        """
        content_output = self.model(generated_image)[-1]
        style_outputs = self.model(generated_image)[:-1]

        content_cost = self.content_cost(content_output)
        style_cost = self.style_cost(style_outputs)

        return self.alpha * content_cost + self.beta * style_cost

    def compute_grads(self, generated_image):
        """
        Computes the gradients of the generated image with respect to the total cost.
        """
        with tf.GradientTape() as tape:
            total_cost = self.total_cost(generated_image)
        gradients = tape.gradient(total_cost, generated_image)
        return gradients, total_cost

    def generate_image(self, iterations=1000, step=None, lr=0.01, beta1=0.9, beta2=0.99):
        """
        Optimizes the generated image over a number of iterations.
        """
        opt = tf.optimizers.Adam(learning_rate=lr, beta_1=beta1, beta_2=beta2)
        generated_image = tf.Variable(self.content_image, dtype=tf.float32)

        for i in range(iterations):
            gradients, cost = self.compute_grads(generated_image)
            opt.apply_gradients([(gradients, generated_image)])

            generated_image.assign(tf.clip_by_value(generated_image, 0.0, 1.0))

            if step is not None and (i + 1) % step == 0:
                print(f"Iteration {i+1}, Total Cost: {cost.numpy()}")

        return generated_image, cost
