#!/usr/bin/env python3
def poly_derivative(poly):
    # Check if poly is a valid list of coefficients
    if not isinstance(poly, list) or len(poly) == 0 or not all(isinstance(x, (int, float)) for x in poly):
        return None

    # If the polynomial is a constant (degree 0), its derivative is 0
    if len(poly) == 1:
        return [0]

    # Calculate the derivative
    derivative = [poly[i] * i for i in range(1, len(poly))]

    return derivative


# Test the function
if __name__ == "__main__":
    poly = [5, 3, 0, 1]
    print(poly_derivative(poly))
