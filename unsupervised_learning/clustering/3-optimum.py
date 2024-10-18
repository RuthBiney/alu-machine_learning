#!/usr/bin/env python3
"""
Defines function that tests for the optimum number of clusters by variance
"""


import numpy as np
kmeans = __import__('1-kmeans').kmeans
variance = __import__('2-variance').variance

def optimum_k(X, kmin=1, kmax=None, iterations=1000):
    if kmax is None or kmax <= kmin:
        return None, None

    results = []
    variances = []

    # Perform K-means clustering for each k
    for k in range(kmin, kmax + 1):
        centroids, labels = kmeans(X, k, iterations)
        results.append((centroids, labels))
        # Calculate the variance for current k
        var = variance(X, centroids)
        variances.append(var)

    # Calculate the differences in variance
    d_vars = [variances[0] - var for var in variances]

    return results, d_vars
