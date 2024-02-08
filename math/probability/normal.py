#!/usr/bin/env python3
"""Represents a normal distribution."""


class Normal:
    """
    Represents a normal distribution.

    Attributes:
    - mean (float): The mean of the distribution.
    - stddev (float): The standard deviation of the distribution.
    """

    def __init__(self, data=None, mean=0., stddev=1.):
        """
        Initializes a Normal distribution.

        """
        if data is None:
            if stddev <= 0:
                raise ValueError("stddev must be a positive value")
            self.mean = float(mean)
            self.stddev = float(stddev)
        else:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")
            self.mean = sum(data) / len(data)
            self.stddev = (
                sum((x - self.mean) ** 2 for x in data) / len(data)) ** 0.5
            if self.stddev <= 0:
                raise ValueError("stddev must be a positive value")

    def pdf(self, x):
        """
        Calculates the value of the PDF for a given x-value.

        Args:
        - x (float): The x-value.

        Returns:
        - float: The PDF value for x.
        """
        exponent = -((x - self.mean) ** 2) / (2 * self.stddev ** 2)
        coefficient = 1 / (self.stddev * (2 * 3.1415926536) ** 0.5)
        return coefficient * (2.7182818285 ** exponent)

    def cdf(self, x):
        """
        Calculates the value of the CDF for a given x-value.

        """
        z = (x - self.mean) / self.stddev
        return (1 + math.erf(z / math.sqrt(2))) / 2
