#!/usr/bin/env python3
"""
Defines function that calculates the expectation step in the EM algorithm
for a Gaussian Mixture Model
"""

import numpy as np
pdf = __import__('5-pdf').pdf

def expectation(X, pi, m, S):
    """
    Calculates the expectation step in the EM algorithm for a GMM

    Parameters:
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

    Returns:
        g, l:
            g [numpy.ndarray of shape (k, n)]: containing the posterior probabilities for each data point in the cluster
            l [float]: total log likelihood
        or None, None on failure
    """
    try:
        n, d = X.shape
        k = pi.shape[0]

        # Check if dimensions match
        if k != m.shape[0] or k != S.shape[0] or d != m.shape[1] or S.shape[1:] != (d, d):
            return None, None

        # Calculate the probability density for each cluster using vectorized operations
        g = np.zeros((k, n))
        for i in range(k):
            g[i] = pi[i] * pdf(X, m[i], S[i])

        # Calculate the total probability for each data point
        total_prob = np.sum(g, axis=0)

        # Check for zero probabilities to avoid division by zero
        if np.any(total_prob == 0):
            return None, None

        # Normalize the posterior probabilities
        g /= total_prob

        # Calculate the log likelihood
        l = np.sum(np.log(total_prob))

        return g, l

    except Exception:
        return None, None
