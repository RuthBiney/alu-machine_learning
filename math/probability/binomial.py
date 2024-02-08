#!/usr/bin/env python3
"""Represents a binomial distribution.,,"""


class Binomial:
    def __init__(self, data=None, n=1, p=0.5):
        # Initialization logic remains the same.
        if data is None:
            if n <= 0:
                raise ValueError("n must be a positive value")
            if not (0 < p < 1):
                raise ValueError("p must be greater than 0 and less than 1")
            self.n = int(n)
            self.p = float(p)
        else:
            # Data processing logic remains the same.
            pass

    def factorial(self, x):
        """Calculate the factorial of a number."""
        if x <= 1:
            return 1
        else:
            return x * self.factorial(x - 1)

    def pmf(self, k):
        """Calculate the PMF for a given number of successes."""
        k = int(k)  # Convert k to an integer to ensure compatibility.
        if k < 0 or k > self.n:  # Validate k is within the range [0, n].
            return 0
        binom_coeff = self.factorial(
            self.n) / (self.factorial(k) * self.factorial(self.n - k))
        pmf_value = binom_coeff * (self.p ** k) * \
            ((1 - self.p) ** (self.n - k))
        return pmf_value


# Example usage
binomial_example = Binomial(n=10, p=0.5)
# For example, calculating PMF for 5 successes in 10 trials with p=0.5
print(binomial_example.pmf(5))
