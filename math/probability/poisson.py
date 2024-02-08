#!/usr/bin/env python3
from math import exp, factorial


class Poisson:
    """
    Represents a Poisson distribution.

    Attributes:
        lambtha (float): The expected number of occurrences in a given time frame.

    Methods:
        __init__(self, data=None, lambtha=1.): Initializes a Poisson distribution.
        pmf(self, k): Calculates the PMF (Probability Mass Function) for a given number of successes.
    """

    def __init__(self, data=None, lambtha=1.):
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
        """
        Calculates the Probability Mass Function (PMF) for a given number of successes.

        Parameters:
            k (int or float): The number of successes for which to calculate the PMF.

        Returns:
            float: The PMF value for k successes, or 0 if k is out of range.
        """
        k = int(k)  # Convert k to an integer
        if k < 0:
            return 0  # Return 0 if k is out of range (negative)

        # Calculate and return the PMF value
        return (self.lambtha ** k) * exp(-self.lambtha) / factorial(k)
