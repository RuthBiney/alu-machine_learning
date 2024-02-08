#!/usr/bin/env python3
"""Represents a binomial distribution.,,"""


class Binomial:
    def __init__(self, data=None, n=1, p=0.5):
        # Assuming the rest of the initialization logic is correct and omitted for brevity.
        self.n = int(n)
        self.p = float(p)

    def factorial(self, x):
        """Calculate the factorial of a number."""
        if x <= 1:
            return 1
        else:
            return x * self.factorial(x - 1)

    def pmf(self, k):
        """Calculate the PMF for a given number of successes."""
        k = int(k)  # Ensure k is an integer.
        if k < 0 or k > self.n:  # Validate k is within the range.
            return 0
        binom_coeff = self.factorial(
            self.n) / (self.factorial(k) * self.factorial(self.n - k))
        pmf_value = binom_coeff * (self.p ** k) * \
            ((1 - self.p) ** (self.n - k))
        return pmf_value
