#!/usr/bin/env python3
"""
Defines function that calculates the expectation step in the EM algorithm
for a Gaussian Mixture Model
"""

import numpy as np
from 5_pdf import pdf

def expectation(X, pi, m, S):
    """
    Perform the expectation step in the EM algorithm for a GMM.

    Parameters:
    - X (numpy.ndarray of shape (n, d)): The data set.
    - pi (numpy.ndarray of shape (k,)): The priors for each cluster.
    - m (numpy.ndarray of shape (k, d)): The centroid means for each cluster.
    - S (numpy.ndarray of shape (k, d, d)): The covariance matrices for each cluster.

    Returns:
    - g (numpy.ndarray of shape (k, n)): The posterior probabilities for each data point in each cluster.
    - l (float): The total log likelihood.
    - None, None on failure.
    """
    try:
        n, d = X.shape
        k = pi.shape[0]
        
        # Initialize the responsibilities matrix (posterior probabilities)
        g = np.zeros((k, n))
        
        # Compute the posterior probabilities for each cluster
        for i in range(k):
            g[i, :] = pi[i] * pdf(X, m[i], S[i])
        
        # Total responsibility across clusters
        g_sum = np.sum(g, axis=0)
        
        # Avoid division by zero or near-zero values in g_sum
        if np.any(g_sum == 0):
            return None, None
        
        # Normalize the responsibilities
        g /= g_sum
        
        # Calculate the log likelihood
        l = np.sum(np.log(g_sum))
        
        return g, l
    except Exception as e:
        return None, None
