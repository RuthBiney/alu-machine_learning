#!/usr/bin/env python3
"""Represents a binomial distribution.,,"""


class Binomial:
    def __init__(self, data=None, n=1, p=0.5):
        if data is None:
            if n <= 0:
                raise ValueError("n must be a positive value")
            if not (0 < p < 1):
                raise ValueError("p must be greater than 0 and less than 1")
            self.n = int(n)
            self.p = float(p)
        else:
            # Placeholder for data processing logic
            pass

    def factorial(self, x):
        """Calculate the factorial of a number."""
        if x <= 1:
            return 1
        else:
            return x * self.factorial(x - 1)

    def pmf(self, k):
        """Calculate the PMF for a given number of successes."""
        k = int(k)  # Ensure k is an integer
        if k < 0 or k > self.n:  # Check if k is out of range
            return 0
        else:
            # Calculate the binomial coefficient
            binom_coeff = self.factorial(
                self.n) / (self.factorial(k) * self.factorial(self.n - k))
            # Calculate PMF using the binomial formula
            pmf_value = binom_coeff * \
                (self.p ** k) * ((1 - self.p) ** (self.n - k))
            return pmf_value
