#!/usr/bin/env python3
'''
Write a function def expectation(X, pi, m, S): that calculates the expectation step in the EM algorithm for a GMM:

X is a numpy.ndarray of shape (n, d) containing the data set
pi is a numpy.ndarray of shape (k,) containing the priors for each cluster
m is a numpy.ndarray of shape (k, d) containing the centroid means for each cluster
S is a numpy.ndarray of shape (k, d, d) containing the covariance matrices for each cluster
You may use at most 1 loop
Returns: g, l, or None, None on failure
g is a numpy.ndarray of shape (k, n) containing the posterior probabilities for each data point in each cluster
l is the total log likelihood
You should use pdf = __import__('5-pdf').pdf
'''

import numpy as np
pdf = __import__('5-pdf').pdf


def expectation(X, pi, m, S):
    if not isinstance(X, np.ndarray) or not isinstance(pi, np.ndarray) or not isinstance(m, np.ndarray) or not isinstance(S, np.ndarray):
        return None, None
    k, d = m.shape
    n = X.shape[0]
    g = np.zeros((k, n))
    l = 0
    for i in range(k):
        g[i] = pi[i] * pdf(X, m[i], S[i])
    l = np.sum(np.log(np.sum(g, axis=0)))
    g /= np.sum(g, axis=0)
    return g, l


initialize = __import__('4-initialize').initialize

if __name__ == '__main__':
    np.random.seed(11)
    a = np.random.multivariate_normal([30, 40], [[75, 5], [5, 75]], size=10000)
    b = np.random.multivariate_normal([5, 25], [[16, 10], [10, 16]], size=750)
    c = np.random.multivariate_normal([60, 30], [[16, 0], [0, 16]], size=750)
    d = np.random.multivariate_normal(
        [20, 70], [[35, 10], [10, 35]], size=1000)
    X = np.concatenate((a, b, c, d), axis=0)
    np.random.shuffle(X)
    pi, m, S = initialize(X, 4)
    g, l = expectation(X, pi, m, S)
    print(g)
    print(np.sum(g, axis=0))
    print(l)
