#!/usr/bin/env python3
""" a function def convolve_grayscale_valid(images, kernel)"""
import numpy as np


def convolve_grayscale_valid(images, kernel):
    """
    Perform a valid convolution on grayscale images.

    Args:
    - images: a numpy.ndarray with shape (m, h, w) containing multiple grayscale images
              m is the number of images
              h is the height in pixels of the images
              w is the width in pixels of the images
    - kernel: a numpy.ndarray with shape (kh, kw) containing the kernel for the convolution
              kh is the height of the kernel
              kw is the width of the kernel

    Returns:
    - convolved_images: a numpy.ndarray containing the convolved images
    """

    m, h, w = images.shape
    kh, kw = kernel.shape

    # Calculate output shape
    output_h = h - kh + 1
    output_w = w - kw + 1

    # Initialize the output array
    output = np.zeros((m, output_h, output_w))

    # Flip the kernel
    kernel = np.flipud(np.fliplr(kernel))

    # Iterate over images
    for i in range(m):
        # Iterate over height
        for j in range(output_h):
            # Iterate over width
            for k in range(output_w):
                # Compute the convolution for the current position
                output[i, j, k] = np.sum(images[i, j:j+kh, k:k+kw] * kernel)

    return output
