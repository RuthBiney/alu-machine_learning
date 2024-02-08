#!/usr/bin/env python3
class Poisson:
    def __init__(self, data=None, lambtha=1.):
        """Calculates the PMF"""
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

    def factorial(self, k):
        """Calculates the factorial of k."""
        result = 1
        for i in range(1, k + 1):
            result *= i
        return result

    def exp(self, x):
        """Approximates the exponential of x using a series expansion."""
        n = 100  # Number of terms for approximation
        return sum((x**i) / self.factorial(i) for i in range(n))

    def pmf(self, k):
        """Calculates the PMF for a given number of successes."""
        k = int(k)  # Convert k to an integer
        if k < 0:
            return 0  # PMF is 0 if k is out of range

        # Calculate PMF using the formula: (lambtha^k * e^(-lambtha)) / k!
        pmf_value = (self.lambtha ** k) * \
            self.exp(-self.lambtha) / self.factorial(k)
        return pmf_value
