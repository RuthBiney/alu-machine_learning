#!/usr/bin/env python3
class Poisson:
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

    def factorial(self, k):
        """Calculates the factorial of k."""
        if k == 0:
            return 1
        else:
            return k * self.factorial(k - 1)

    def pmf(self, k):
        """Calculates the PMF for a given number of successes."""
        k = int(k)  # Ensure k is an integer
        if k < 0:
            return 0  # PMF is 0 if k is out of range

        # Calculate PMF using the formula: (lambtha^k * e^(-lambtha)) / k!
        lambtha = self.lambtha
        e_minus_lambtha = self.exp(-lambtha)
        lambtha_k = lambtha ** k
        k_factorial = self.factorial(k)
        pmf_value = (lambtha_k * e_minus_lambtha) / k_factorial
        return pmf_value

    def exp(self, x):
        """Approximates the exponential of x using a series expansion."""
        n = 100  # Number of terms for approximation
        return sum((x**i) / self.factorial(i) for i in range(n))
