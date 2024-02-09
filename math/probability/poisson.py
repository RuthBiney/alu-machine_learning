#!/usr/bin/env python3
"""Poisson Distribution"""


class Poisson:
    def __init__(self, data=None, lambtha=1.):
        """ Class Poisson that represents a distribution of Poisson"""
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
            if self.lambtha <= 0:
                raise ValueError("lambtha must be a positive value")

    def pmf(self, k):
        """Calculate pmf"""
        k = int(k)
        if k < 0:
            return 0
        else:
            return (self.lambtha ** k) * (2.7182818285 ** (-self.lambtha)) / self.factorial(k)

    def factorial(self, n):
        """Calculate factorial"""
        if n == 0:
            return 1
        else:
            return n * self.factorial(n - 1)


# Test cases
if __name__ == "__main__":
    p = Poisson(data=[1, 2, 3])
    print("{:.10f}".format(p.pmf(2)))  # Should print the PMF value for k = 2
    print("{:.10f}".format(p.pmf(1.5)))  # Should print the PMF value for k = 1
