#!/usr/bin/env python3
"""
    The function def create_confusion_matrix(labels, logits):
    that creates a confusion matrix:
"""


import numpy as np


def create_confusion_matrix(labels, logits):
    """
    A function that creates a confusion matrix:

    """
    return np.matmul(labels.T, logits)
