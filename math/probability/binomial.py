#!/usr/bin/env python3
"""Binomial distribution"""


class Binomial:
    def __init__(self, data=None, n=1, p=0.5):
        """
        Constructor for the Binomial class.

        """
        if data is None:
            if n < 1:
                raise ValueError("n must be a positive value")
            else:
                self.n = n
            if p <= 0 or p >= 1:
                raise ValueError("p must be greater than 0 and less than 1")
            else:
                self.p = p
        else:
            if not isinstance(data, list):
                raise TypeError('data must be a list')
            if len(data) < 2:
                raise ValueError('data must contain multiple values')
            mean = sum(data) / len(data)
            variance = sum((x - mean) ** 2 for x in data) / len(data)
            q = variance / mean
            p = 1 - q
            self.n = round(mean / p)
            self.p = mean / self.n

    def pmf(self, k):
        """
        Calculates the probability mass function (PMF).

        """
        if not isinstance(k, int):
            k = int(k)
        if k < 0:
            return 0
        binom_coeff = self._binomial_coefficient(k)
        pmf = binom_coeff * (self.p ** k) * ((1 - self.p) ** (self.n - k))
        return pmf

    def _binomial_coefficient(self, k):
        """
        Calculates the binomial coefficient (n choose k).

        Parameters:
            k (int): Number of successes.

        Returns:
            int: Binomial coefficient.
        """
        n_fact = self._factorial(self.n)
        k_fact = self._factorial(k)
        n_minus_k_fact = self._factorial(self.n - k)
        return n_fact // (k_fact * n_minus_k_fact)

    def _factorial(self, x):
        """
        Calculates the factorial of a number x.

        """
        if x == 0:
            return 1
        result = 1
        for i in range(1, x + 1):
            result *= i
        return result

    def cdf(self, k):
        """
        Calculates the cumulative distribution function (CDF) 

        """
        if not isinstance(k, int):
            k = int(k)
        if k < 0:
            return 0
        cdf = sum(self.pmf(i) for i in range(k + 1))
        return cdf


# Example usage
if __name__ == "__main__":
    b = Binomial(data=[84, 85])
    print(b.pmf(84))  # Expected output: 2.5827623561e-10
    print(b.pmf(85))  # Expected output: 1.6516512762e-11
    print(b.cdf(84))  # Expected output: 0.0990153774
