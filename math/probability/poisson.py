#!/usr/bin/env python3
from math import exp, factorial


class Poisson:

    "Represents a Poisson distribution."

    def __init__(self, data=None, lambtha=1.):
        "Initializes the Poisson distribution either by estimating lambtha"

        if data is None:
            if lambtha <= 0:
                raise ValueError("lambtha must be a positive value")
            self.lambtha = float(lambtha)
        else:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")
            self.lambtha = float(sum(data) / len(data))

    def pmf(self, k):
        "Calculates the Probability Mass Function (PMF)"

        k = int(k)  # Ensure k is an integer
        if k < 0:
            return 0  # Return 0 if k is out of range (negative)
        else:
            # Calculate and return the PMF value
            return (self.lambtha ** k) * exp(-self.lambtha) / factorial(k)
