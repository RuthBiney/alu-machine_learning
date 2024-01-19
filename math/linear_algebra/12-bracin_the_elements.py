#!/usr/bin/env python3

"import numpy as np"


def np_elementwise(mat1, mat2):
    """A function that performs  element wise addition"""
    elementwise_sum = mat1 + mat2
    elementwise_diff = mat1 - mat2
    elementwise_prod = mat1 * mat2
    elementwise_quot = mat1 / mat2

    return (elementwise_sum,
            elementwise_diff,
            elementwise_prod,
            elementwise_quot)
