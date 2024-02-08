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
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")
            # Calculate n and p from the data
            self.n = len(data)
            self.p = sum(data) / len(data)

    def pmf(self, k):
        """
        Calculate the value of the PMF for a given number of successes k.

        Parameters:
            k (int): The number of successes.

        Returns:
            float: The PMF value for k.
        """
        k = int(k)  # Convert k to an integer
        if k < 0 or k > self.n:  # Check if k is out of range
            return 0
        binom_coeff = self._binomial_coefficient(k)
        pmf_value = binom_coeff * (self.p ** k) * \
            ((1 - self.p) ** (self.n - k))
        return pmf_value

    def _binomial_coefficient(self, k):
        """
        Calculate the binomial coefficient (n choose k).

        Parameters:
            k (int): The number of successes.

        Returns:
            int: The binomial coefficient.
        """
        return self._factorial(self.n) / (self._factorial(k) * self._factorial(self.n - k))

    def _factorial(self, x):
        """
        Calculate the factorial of a number x.

        Parameters:
            x (int): The number to calculate the factorial of.

        Returns:
            int: The factorial of x.
        """
        if x == 0:
            return 1
        result = 1
        for i in range(1, x + 1):
            result *= i
        return result


# Example usage:
if __name__ == "__main__":
    import numpy as np
    np.random.seed(0)
    data = np.random.binomial(50, 0.6, 100).tolist()
    b1 = Binomial(data)
    print('P(30):', b1.pmf(30))

    b2 = Binomial(n=50, p=0.6)
    print('P(30):', b2.pmf(30))
