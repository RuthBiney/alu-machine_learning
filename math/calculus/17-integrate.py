#!/usr/bin/env python3
def poly_integral(poly, C=0):
    # Check if the input is valid
    if not isinstance(poly, list) or not all(isinstance(coeff, (int, float)) for coeff in poly) or not isinstance(C, (int, float)):
        return None

    # Check if the polynomial is not empty
    if len(poly) == 0:
        return None

    # Calculate the integral
    integral_poly = [C]  # Start with the integration constant
    for power, coeff in enumerate(poly):
        if coeff == 0:
            integral_poly.append(0)
        else:
            # The integral of x^n is x^(n+1)/(n+1)
            integral_coeff = coeff / (power + 1)
            # If the integral coefficient is a whole number, convert it to an integer
            integral_coeff = int(
                integral_coeff) if integral_coeff.is_integer() else integral_coeff
            integral_poly.append(integral_coeff)

    # Remove trailing zeroes to make the list as small as possible
    while len(integral_poly) > 1 and integral_poly[-1] == 0:
        integral_poly.pop()

    return integral_poly


# Example usage:
poly = [5, 3, 0, 1]
print(poly_integral(poly))  # This should print [0, 5, 1.5, 0, 0.25]
