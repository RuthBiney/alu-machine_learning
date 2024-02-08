#!/usr/bin/env python3
class Poisson:
    """
    Represents a Poisson distribution.

    Attributes:
        lambtha (float): The expected number of occurrences in a given time frame.

    Methods:
        __init__(self, data=None, lambtha=1.): Initializes a Poisson distribution.
        pmf(self, k): Calculates the PMF (Probability Mass Function) for a given number of successes without using external imports.
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

    def factorial(self, n):
        """Calculates factorial of n (n!) without using external imports."""
        if n == 0:
            return 1
        else:
            return n * self.factorial(n-1)

    def exp(self, x):
        """Calculates the exponential of x using a series expansion."""
        n_terms = 10  # Number of terms to include in the series expansion for approximation
        return sum(x**i / self.factorial(i) for i in range(n_terms))

    def pmf(self, k):
        """
        Calculates the Probability Mass Function (PMF)
        """
        k = int(k)  # Convert k to an integer
        if k < 0:
            return 0  # Return 0 if k is out of range (negative)

        # Calculate and return the PMF value without using external imports
        return (self.lambtha ** k) * self.exp(-self.lambtha) / self.factorial(k)
