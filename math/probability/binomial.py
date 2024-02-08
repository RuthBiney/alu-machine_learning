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
            # Data processing logic here
            pass

    def factorial(self, n):
        """Calculate the factorial of n."""
        if n == 0:
            return 1
        else:
            return n * self.factorial(n-1)

    def pmf(self, k):
        """Calculate the PMF for a given number of successes k."""
        k = int(k)
        if k < 0 or k > self.n:
            return 0
        binom_coeff = self.factorial(
            self.n) / (self.factorial(k) * self.factorial(self.n - k))
        pmf_value = binom_coeff * (self.p ** k) * \
            ((1 - self.p) ** (self.n - k))
        return pmf_value


# Example usage:
binomial = Binomial(n=50, p=0.04)  # Hypothetical scenario
print(binomial.pmf(2))  # Hypothetical k value
