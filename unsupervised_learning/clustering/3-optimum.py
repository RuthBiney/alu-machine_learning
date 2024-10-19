#!/usr/bin/env python3
"""Testing for the optimum number of clusters"""

import numpy as np
kmeans = __import__('1-kmeans').kmeans
variance = __import__('2-variance').variance


def optimum_k(X, kmin=1, kmax=None, iterations=1000):
    # Validate input parameters
    if not isinstance(kmin, int) or kmin <= 0:
        return None, None
    if kmax is not None and (not isinstance(kmax, int) or kmax < kmin):
        return None, None

    # Set kmax to the number of data points if not provided
    if kmax is None:
        kmax = X.shape[0]

    # Lists to store results and variance calculations
    results = []
    variances = []

    # Loop through each value of k from kmin to kmax
    for k in range(kmin, kmax + 1):
        # Perform K-means clustering
        centroids, labels = kmeans(X, k, iterations=iterations)
        results.append((centroids, labels))

        # Calculate variance for the current k
        current_variance = variance(X, centroids)
        variances.append(current_variance)

    # Calculate the variance differences (delta variance)
    initial_variance = variances[0]
    d_vars = [initial_variance - v for v in variances]

    return results, d_vars
