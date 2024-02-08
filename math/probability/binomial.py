#!/usr/bin/env python3
"""Represents a binomial distribution.,,"""


class Binomial:
    """
    Represents a binomial distribution.

    Attributes:
    - n (int): The number of Bernoulli trials.
    - p (float): The probability of success.
    """

    def __init__(self, data=None, n=1, p=0.5):
        """
        Initializes a Binomial distribution.

        Args:
        - data (list, optional): The data used to estimate the distribution.
        - n (int, optional): The number of Bernoulli trials.
        - p (float, optional): The probability of success.

        Raises:
        - ValueError: If n is not a positive value.
                      If p is not a valid probability.
                      If data is given but does not contain at least two data points.
        - TypeError: If data is given but not a list.
        """
        if data is None:
            if n <= 0:
                raise ValueError("n must be a positive value")
            if not 0 < p < 1:
                raise ValueError("p must be greater than 0 and less than 1")
            self.n = round(n)  # Round n to the nearest integer
            self.p = p
        else:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain at least two values")

            # Calculate p first
            p = sum(data) / len(data)
            # Then calculate n
            n = round(sum(data) / p)
            # Recalculate p to get the precise value
            p = sum(data) / n

            if n <= 0:
                raise ValueError("n must be a positive value")
            if not 0 < p < 1:
                raise ValueError("p must be greater than 0 and less than 1")

            self.n = round(n)  # Round n to the nearest integer
            self.p = p

    def pmf(self, k):
        """
        Calculates the value of the PMF for a given number of successes.

        Args:
        - k (int): The number of successes.

        Returns:
        - float: The PMF value for k.
        """
        # Convert k to integer
        k = int(k)

        # Check if k is out of range
        if k < 0 or k > self.n:
            return 0

        # Calculate the binomial coefficient
        from math import comb
        coefficient = comb(self.n, k)

        # Calculate the PMF value using the binomial distribution formula
        pmf_value = coefficient * (self.p ** k) * \
            ((1 - self.p) ** (self.n - k))

        return pmf_value


# Test cases
if __name__ == "__main__":
    try:
        binomial1 = Binomial(n=-2)
    except ValueError as ve:
        print(ve)  # Should raise "n must be a positive value"

    try:
        binomial2 = Binomial(p=0.2)
    except ValueError as ve:
        print(ve)  # Should raise "p must be greater than 0 and less than 1"

    try:
        binomial3 = Binomial(data=[0.4])
    except ValueError as ve:
        print(ve)  # Should raise "data must contain at least two values"

    binomial4 = Binomial(data=[1, 1, 1, 1])
    print(binomial4.n, binomial4.p)  # Should print the calculated n and p

    binomial5 = Binomial(data=[84, 84, 84, 84, 85, 85, 85, 85, 85])
    print(binomial5.n, binomial5.p)  # Should print the calculated n and p

    print(binomial4.pmf(2))  # Should print the PMF value for k = 2
    print(binomial5.pmf(84))  # Should print the PMF value for k = 84
