#!/usr/bin/env python3
'''
    a function def poly_derivative(poly):
    that calculates the derivative of a polynomial

    Parameters:
    poly (list): A list of coefficients.
'''


def poly_derivative(poly):
    # Check if poly is not a list or is an empty list
    if not isinstance(poly, list) or not poly:
        return None
    if len(poly) == 1:
        return [0]

    return [poly[i] * i for i in range(1, len(poly))]
