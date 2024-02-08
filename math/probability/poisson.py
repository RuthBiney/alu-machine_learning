#!/usr/bin/env python3
class Poisson:
    """
    Represents a Poisson distribution.

    Attributes:
        lambtha (float): The expected number of occurrences in a given time frame.

    Methods:
        __init__(self, data=None, lambtha=1.): Initializes a Poisson distribution.
    """

    def __init__(self, data=None, lambtha=1.):
        """
        Initializes the Poisson distribution either by estimating lambtha from data
        or using a provided lambtha value.

        Parameters:
            data (list, optional): A list of data points to estimate lambtha. Default is None.
            lambtha (float, optional): The expected number of occurrences in a given time frame.
                                       This is used if data is None. Default is 1.

        Raises:
            ValueError: If lambtha is not a positive value when data is None.
            TypeError: If data is provided but is not a list.
            ValueError: If data is provided but does not contain multiple values.
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
            self.lambtha = float(sum(data) / len(data))
