#!/usr/bin/env python3
"""Testing for the optimum number of clusters"""

import numpy as np
kmeans = __import__('1-kmeans').kmeans
variance = __import__('2-variance').variance


def optimum_k(X, kmin=1, kmax=None, iterations=1000):
    # Check for valid kmin and kmax
    if not isinstance(kmin, int) or kmin <= 0 or (kmax is not None and not isinstance(kmax, int)):
        return None, None
    if kmax is None:
        kmax = X.shape[0]
    if kmax < kmin or kmax <= 1:
        return None, None

    # List to hold the results of K-means for each cluster size
    results = []
    # List to hold the variance for each cluster size
    variances = []

    # Initial K-means clustering and variance calculation for kmin
    for k in range(kmin, kmax + 1):
        centroids, labels = kmeans(X, k, iterations=iterations)
        results.append((centroids, labels))
        current_variance = variance(X, centroids)
        variances.append(current_variance)

    # Calculate the difference in variance from the smallest cluster size
    d_vars = [variances[0] - v for v in variances]

    return results, d_vars
