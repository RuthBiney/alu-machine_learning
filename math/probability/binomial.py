#!/usr/bin/env python3
"""Represents a binomial distribution.,,"""


class Binomial:
    """
    A class to represent a binomial distribution.

    Attributes:
        n (int): Number of Bernoulli trials.
        p (float): Probability of a success in each trial.


    """

    def __init__(self, data=None, n=1, p=0.5):
        """
        The constructor for Binomial class.

        Raises:
            ValueError: If 'n' is not a positive value.
            ValueError: If 'p' is not in the range (0, 1).
            TypeError: If 'data' is not a list when provided.
            ValueError: If 'data' does not contain at least two values.


        """

        if data is None:
            # Validate 'n' and 'p' when no data is provided
            if n <= 0:
                raise ValueError("n must be a positive value")
            if not (0 < p < 1):
                raise ValueError("p must be greater than 0 and less than 1")
            self.n = int(n)  # Save 'n' as an integer
            self.p = float(p)  # Save 'p' as a float
        else:
            # Validate 'data'
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")

            # Calculate 'p' as the mean of successes per trial in the data
            mean_data = sum(data) / len(data)

            # Initial calculation of 'n' and 'p' based on the data provided
            variance_data = sum((xi - mean_data) **
                                2 for xi in data) / len(data)
            p_initial = 1 - variance_data / mean_data
            n_initial = round(mean_data / p_initial)

            # Recalculate 'p' with the rounded 'n' value for accuracy
            p_final = mean_data / n_initial

            self.n = n_initial  # Set the calculated 'n'
            self.p = p_final  # Set the recalculated 'p'
