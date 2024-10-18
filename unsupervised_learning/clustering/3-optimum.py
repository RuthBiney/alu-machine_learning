#!/usr/bin/env python3
"""
Defines function that tests for the optimum number of clusters by variance
"""

def optimum_k(X, kmin=1, kmax=None, iterations=1000):
    """
    Tests for the optimum number of clusters by variance.

    Parameters:
        X [numpy.ndarray of shape (n, d)]: contains the dataset used for K-means clustering
            n: the number of data points
            d: the number of dimensions for each data point
        kmin [positive int]: containing the minimum number of clusters to check for (inclusive)
        kmax [positive int]: containing the maximum number of clusters to check for (inclusive)        iterations [positive int]: containing the maximum number of iterations for K-means

    Returns:
        results, d_vars:
            results [list]: containing the output of K-means for each cluster size
            d_vars [list]: containing the difference in variance from the smallest cluster size for each cluster size
        or None, None on failure
    """
    if kmax is None or kmax < kmin or kmin < 1:
        return None, None

    results = []
    variances = []

    # Perform K-means clustering for each k
    for k in range(kmin, kmax + 1):
        centroids, labels = kmeans(X, k, iterations)
        results.append((centroids, labels))
        # Calculate the variance for the current number of clusters
        var = variance(X, centroids)
        variances.append(var)

    # Calculate the difference in variance from the smallest number of clusters
    d_vars = [variances[0] - var for var in variances]

    return results, d_vars