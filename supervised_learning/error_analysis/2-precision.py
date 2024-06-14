#!/usr/bin/env python3
"""
    A function def precision(confusion):
    that calculates the precision for each class in
    a confusion matrix
"""


import numpy as np


def precision(confusion):
    """
    A function def precision(confusion):
    that calculates the precision for each class in
    a confusion matrix

    """
    return np.diag(confusion) / np.sum(confusion, axis=0)
