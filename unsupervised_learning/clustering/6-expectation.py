#!/usr/bin/env python3
"""
Defines function that calculates the expectation step in the EM algorithm
for a Gaussian Mixture Model
"""

import numpy as np
pdf = __import__('5-pdf').pdf

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
        n, d = X.shape  # number of data points and dimensions
        k = pi.shape[0]  # number of clusters
        
        # Initialize the responsibility matrix (posterior probabilities)
        g = np.zeros((k, n))
        
        # Calculate the likelihood for each cluster and each data point
        for i in range(k):
            g[i, :] = pi[i] * pdf(X, m[i], S[i])
        
        # Compute the total likelihood for each data point (denominator for normalizing)
        g_sum = np.sum(g, axis=0)
        
        # Check for zero values to avoid division by zero
        if np.any(g_sum == 0):
            return None, None
        
        # Normalize the responsibilities (posterior probabilities)
        g /= g_sum
        
        # Compute the total log likelihood
        log_likelihood = np.sum(np.log(g_sum))
        
        return g, log_likelihood
    
    except Exception:
        return None, None