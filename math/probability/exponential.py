#!/usr/bin/env python3
"""Represents an exponential distribution."""


class Exponential:
    """
    Represents an exponential distribution.

    """

    def __init__(self, data=None, lambtha=1.):
        """
        Initializes an Exponential distribution.

        """
        if data is None:
            if lambtha <= 0:
                raise ValueError("lambtha must be a positive value")
            self.lambtha = float(lambtha)
        else:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")
            self.lambtha = 1 / (sum(data) / len(data))
            if self.lambtha <= 0:
                raise ValueError("lambtha must be a positive value")


# Test cases
if __name__ == "__main__":
    exp5 = Exponential(data=[2, 3, 4])
    print("{:.10f}".format(exp5.lambtha))  # Should print 5.2902751279
    exp6 = Exponential(data=[1, 2, 3, 4, 5])
    print("{:.10f}".format(exp6.lambtha))  # Should print 5.5528992355
