#!/usr/bin/env python3
"""
    A function def f1_score(confusion):
    that calculates the F1 score of a confusion matrix
"""


sensitivity = __import__('1-sensitivity').sensitivity
precision = __import__('2-precision').precision


def f1_score(confusion):
    """
    A function def f1_score(confusion):
    that calculates the F1 score of a confusion matrix

    """
    return 2 * precision(confusion) * sensitivity(confusion) / \
        (precision(confusion) + sensitivity(confusion))
