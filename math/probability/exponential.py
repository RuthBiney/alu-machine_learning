#!/usr/bin/env python3
class Exponential:

    "Represents an exponential distribution."

    def __init__(self, data=None, lambtha=1.):
        """
        Initializes an Exponential distribution.

        """
        if data is None:
            if lambtha <= 0:
                raise ValueError("lambtha must be a positive value")
            self.lambtha = float(lambtha)
        else:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")
            self.lambtha = 1 / (sum(data) / len(data))
            if self.lambtha <= 0:
                raise ValueError("lambtha must be a positive value")


# Test cases
try:
    exp1 = Exponential(data=[1])
except ValueError as ve:
    print(ve)  # Should raise "data must contain multiple values"

try:
    exp2 = Exponential(data="not a list")
except TypeError as te:
    print(te)  # Should raise "data must be a list"

try:
    exp3 = Exponential(lambtha=-3)
except ValueError as ve:
    print(ve)  # Should raise "lambtha must be a positive value"

exp4 = Exponential(lambtha=2)
print(exp4.lambtha)  # Should print 2.0
