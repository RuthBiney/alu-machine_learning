#!/usr/bin/env python3
"""
Defines function that calculates the expectation step in the EM algorithm
for a Gaussian Mixture Model
"""


import numpy as np
pdf = __import__('5-pdf').pdf

def expectation(X, pi, m, S):
    """
    Calculates the expectation step in the EM algorithm for a GMM.

    parameters:
        X [numpy.ndarray of shape (n, d)]:
            contains the dataset
            n: the number of data points
            d: the number of dimensions for each data point
        pi [numpy.ndarray of shape (k,)]:
            contains the priors for each cluster
        m [numpy.ndarray of shape (k, d)]:
            contains the centroid means for each cluster
        S [numpy.ndarray of shape (k, d, d)]:
            contains the covariance matrices for each cluster

    should only use one loop

    returns:
        g, l:
            g [numpy.ndarray of shape (k, n)]:
                containing the posterior probabilities for each data point
                    in the cluster
            l [float]:
                total log likelihood
        or None, None on failure
    """
    try:
        n, d = X.shape  # number of data points and dimensions
        k = pi.shape[0]  # number of clusters
        
        # Initialize g to store posterior probabilities
        g = np.zeros((k, n))

        # Compute the posterior probabilities using the priors, means, and covariance matrices
        for i in range(k):
            g[i] = pi[i] * pdf(X, m[i], S[i])

        # Sum across clusters for normalization
        g_sum = np.sum(g, axis=0)

        # Check for zero values to avoid division by zero
        if np.any(g_sum == 0):
            return None, None
        
        # Normalize to get the posterior probabilities
        g /= g_sum

        # Calculate the total log likelihood
        log_likelihood = np.sum(np.log(g_sum))
        
        return g, log_likelihood
    
    except Exception as e:
        return None, None
