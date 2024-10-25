#!/usr/bin/env python3
""" baum_welch algorithm"""

import numpy as np


def forward(Observation, Emission, Transition, Initial):
    """ Forward function based on task3 """
    N = Transition.shape[0]  # Hidden States
    T = Observation.shape[0]  # Observations
    F = np.zeros((N, T))
    F[:, 0] = Initial.T * Emission[:, Observation[0]]

    for t in range(1, T):
        for n in range(N):
            F[n, t] = np.sum(Transition[:, n] * F[:, t - 1]) * \
                Emission[n, Observation[t]]
    return F


def backward(Observation, Emission, Transition, Initial):
    """ Backward function based on task5 """
    T = Observation.shape[0]
    N, _ = Emission.shape
    beta = np.zeros((N, T))
    beta[:, T - 1] = np.ones(N)

    for t in range(T - 2, -1, -1):
        for n in range(N):
            beta[n, t] = np.sum(Transition[n, :] * beta[:, t + 1]
                                * Emission[:, Observation[t + 1]])
    return beta


def baum_welch(Observations, Transition, Emission, Initial, iterations=1000):
    """
    Baum-Welch algorithm for a hidden Markov model
    """
    N, M = Emission.shape
    T = Observations.shape[0]

    for _ in range(iterations):
        alpha = forward(Observations, Emission, Transition, Initial)
        beta = backward(Observations, Emission, Transition, Initial)

        xi = np.zeros((N, N, T - 1))
        for t in range(T - 1):
            denominator = np.dot(np.dot(
                alpha[:, t].T, Transition) * Emission[:, Observations[t + 1]].T, beta[:, t + 1]) + 1e-8
            for i in range(N):
                numerator = alpha[i, t] * Transition[i, :] * \
                    Emission[:, Observations[t + 1]].T * beta[:, t + 1].T
                xi[i, :, t] = numerator / denominator

        gamma = np.sum(xi, axis=1)
        Transition = np.sum(xi, 2) / np.sum(gamma,
                                            axis=1).reshape((-1, 1)) + 1e-8

        gamma = np.hstack(
            (gamma, np.sum(xi[:, :, T - 2], axis=0).reshape((-1, 1))))

        denominator = np.sum(gamma, axis=1) + 1e-8
        for s in range(M):
            Emission[:, s] = np.sum(gamma[:, Observations == s], axis=1)
        Emission = np.divide(Emission, denominator.reshape((-1, 1)) + 1e-8)

    return Transition, Emission
