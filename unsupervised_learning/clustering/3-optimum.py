#!/usr/bin/env python3
"""Testing for the optimum number of clusters"""

import numpy as np
kmeans = __import__('1-kmeans').kmeans
variance = __import__('2-variance').variance


def optimum_k(X, kmin=1, kmax=None, iterations=1000):
    # Validate input
    if not isinstance(X, np.ndarray) or len(X.shape) != 2:
        return None, None
    if not isinstance(kmin, int) or kmin < 1:
        return None, None
    if kmax is None or not isinstance(kmax, int) or kmax < kmin:
        return None, None
    if not isinstance(iterations, int) or iterations < 1:
        return None, None

    # Initialize lists to store results
    results = []
    variances = []

    # Iterate over cluster sizes
    for k in range(kmin, kmax + 1):
        # Apply K-means clustering
        centroids, labels = kmeans(X, k, iterations=iterations)
        # Calculate the variance for the current clustering
        var = variance(X, centroids)
        # Store the results
        results.append((centroids, labels))
        variances.append(var)

    # Calculate the difference in variance from the smallest cluster size
    d_vars = [variances[0] - var for var in variances]

    return results, d_vars
