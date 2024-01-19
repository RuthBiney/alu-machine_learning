#!/usr/bin/env python3

import numpy as np
"""A function that concatenates two matrices at specific axis"""


def np_cat(mat1, mat2, axis=0):
    """A function that concatenates two matrices at specific axis"""
    return np.concatenate((mat1, mat2), axis=axis)
