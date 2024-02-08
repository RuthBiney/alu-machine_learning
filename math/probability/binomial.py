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

        """
        if data is None:
            if n <= 0:
                raise ValueError("n must be a positive value")
            if not 0 < p < 1:
                raise ValueError("p must be greater than 0 and less than 1")
            self.n = int(n)
            self.p = float(p)
        else:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")
            p = sum(data) / len(data)
            n = round(sum(data) / p)
            p = sum(data) / n
            self.n = int(n)
            self.p = p


# Test cases
if __name__ == "__main__":
    try:
        binomial1 = Binomial(n=-2)
    except ValueError as ve:
        print(ve)  # Should raise "n must be a positive value"

    try:
        binomial2 = Binomial(p=0.2)
    except ValueError as ve:
        print(ve)  # Should raise "data must contain multiple values"

    try:
        binomial3 = Binomial(data=[0.4])
    except ValueError as ve:
        print(ve)  # Should raise "data must contain multiple values"

    binomial4 = Binomial(data=[1, 1, 1, 1])
    print(binomial4.n, binomial4.p)  # Should print the calculated n and p

    binomial5 = Binomial(data=[84, 84, 84, 84, 85, 85, 85, 85, 85])
    print(binomial5.n, binomial5.p)  # Should print the calculated n and p
