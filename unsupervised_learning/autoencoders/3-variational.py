#!/usr/bin/env python3
""" Variational Autoencoder"""

import tensorflow.keras as keras


def autoencoder(input_dims, hidden_layers, latent_dims):
    """
    function that creates a variational autoencoder
    Args:
        input_dims: integer containing the dimensions of the model input
        hidden_layers:  list containing the number of nodes for each hidden
                        layer in the encoder, respectively
        latent_dims: integer containing the dimensions of the latent space
                     representation
    Returns: encoder, decoder, auto
    """

    X_input = keras.Input(shape=(input_dims,))
    Y_prev = X_input

    # Encoder network
    for units in hidden_layers:
        hidden_ly = keras.layers.Dense(units=units, activation='relu')
        Y_prev = hidden_ly(Y_prev)

    # Latent space representation
    z_mean = keras.layers.Dense(units=latent_dims, activation=None)(Y_prev)
    z_log_sigma = keras.layers.Dense(
        units=latent_dims, activation=None)(Y_prev)

    def sampling(args):
        """Sampling similar points in latent space"""
        z_m, z_stand_dev = args
        batch = keras.backend.shape(z_m)[0]
        dim = keras.backend.int_shape(z_m)[1]
        epsilon = keras.backend.random_normal(shape=(batch, dim))
        return z_m + keras.backend.exp(z_stand_dev / 2) * epsilon

    z = keras.layers.Lambda(sampling,
                            output_shape=(latent_dims,))([z_mean,
                                                          z_log_sigma])
    encoder = keras.Model(X_input, [z, z_mean, z_log_sigma])

    # Decoder network
    X_decode = keras.Input(shape=(latent_dims,))
    Y_prev = X_decode
    for units in reversed(hidden_layers):
        hidden_ly_deco = keras.layers.Dense(units=units, activation='relu')
        Y_prev = hidden_ly_deco(Y_prev)

    output = keras.layers.Dense(units=input_dims, activation='sigmoid')(Y_prev)
    decoder = keras.Model(X_decode, output)

    # Variational Autoencoder
    e_output = encoder(X_input)[0]  # Use z as the encoded output
    d_output = decoder(e_output)
    auto = keras.Model(X_input, d_output)

    def vae_loss(x, x_decoder_mean):
        x_loss = keras.backend.binary_crossentropy(x, x_decoder_mean)
        x_loss = keras.backend.sum(x_loss, axis=-1)
        kl_loss = -0.5 * keras.backend.sum(
            1 + z_log_sigma - keras.backend.square(z_mean) - keras.backend.exp(z_log_sigma), axis=-1)
        return x_loss + kl_loss

    auto.compile(optimizer='adam', loss=vae_loss)
    return encoder, decoder, auto
