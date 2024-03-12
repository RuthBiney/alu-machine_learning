#!/usr/bin/env python3

import numpy as np


class MultiNormal:
    """
    Represents a Multivariate Normal distribution.

    Attributes:
    -----------
    mean : numpy.ndarray
        A numpy array of shape (d, 1) containing the mean of the data.
    cov : numpy.ndarray
        A numpy array of shape (d, d) containing the covariance matrix of the data.

    Methods:
    --------
    __init__(self, data)
        Initializes the MultiNormal instance with data, calculates the mean and covariance matrix.

    Parameters:
    -----------
    data : numpy.ndarray
        A 2D numpy array of shape (d, n) containing the dataset, where n is the number of data points
        and d is the number of dimensions in each data point.
    """

    def __init__(self, data):
        """
        Initializes the MultiNormal instance.

        Parameters:
        -----------
        data : numpy.ndarray
            The dataset to model with a Multivariate Normal distribution.

        Raises:
        -------
        TypeError
            If the data is not a 2D numpy.ndarray.
        ValueError
            If the data does not contain multiple data points (n < 2).
        """
        # Check if data is a 2D numpy.ndarray
        if not isinstance(data, np.ndarray) or data.ndim != 2:
            raise TypeError("data must be a 2D numpy.ndarray")
        # Check if data contains multiple data points
        if data.shape[1] < 2:
            raise ValueError("data must contain multiple data points")

        # Calculate the mean of the data
        self.mean = np.mean(data, axis=1, keepdims=True)

        # Manually compute the covariance matrix
        centered_data = data - self.mean
        self.cov = (centered_data @ centered_data.T) / (data.shape[1] - 1)


# Example of how to use the MultiNormal class
if __name__ == "__main__":
    try:
        # Example data
        data = np.array([[1, 2, 3], [2, 3, 4]])
        multi_normal = MultiNormal(data)

        print("Mean:\n", multi_normal.mean)
        print("Covariance Matrix:\n", multi_normal.cov)
    except Exception as e:
        print(e)
