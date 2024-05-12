#!/usr/bin/env python3
import numpy as np

class Neuron:
    def __init__(self, nx):
        """
        Constructor for Neuron class.

        Args:
        nx (int): Number of input features to the neuron.

        Raises:
        TypeError: If nx is not an integer.
        ValueError: If nx is less than 1.
        """
        if not isinstance(nx, int):
            raise TypeError("nx must be an integer")
        if nx < 1:
            raise ValueError("nx must be a positive integer")
        
        # Initialize the weights vector with random normal values
        self.W = np.random.randn(nx).reshape(1, nx)
        # Initialize the bias to 0
        self.b = 0
        # Initialize the activated output to 0
        self.A = 0

# Example usage:
try:
    neuron = Neuron(5)  # Creating a neuron with 5 input features
    print("Weights:", neuron.W)
    print("Bias:", neuron.b)
    print("Activated Output:", neuron.A)
except Exception as e:
    print(e)
