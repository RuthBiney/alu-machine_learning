#!/usr/bin/env python3
""" baum_welch algorithm"""

import numpy as np


def forward(Observation, Emission, Transition, Initial):
    """ Forward algorithm """
    N = Transition.shape[0]  # Number of hidden states
    T = Observation.shape[0]  # Number of observations
    F = np.zeros((N, T))
    F[:, 0] = Initial.T * Emission[:, Observation[0]]

    for t in range(1, T):
        for n in range(N):
            F[n, t] = np.sum(F[:, t - 1] * Transition[:, n]) * \
                Emission[n, Observation[t]]
    return F


def backward(Observation, Emission, Transition, Initial):
    """ Backward algorithm """
    T = Observation.shape[0]
    N, _ = Emission.shape
    beta = np.zeros((N, T))
    beta[:, T - 1] = 1

    for t in range(T - 2, -1, -1):
        for n in range(N):
            beta[n, t] = np.sum(
                Transition[n, :] * Emission[:, Observation[t + 1]] * beta[:, t + 1])
    return beta


def baum_welch(Observations, Transition, Emission, Initial, iterations=1000, tol=1e-6):
    """ Baum-Welch algorithm for a hidden Markov model """
    N, M = Emission.shape
    T = Observations.shape[0]

    for _ in range(iterations):
        alpha = forward(Observations, Emission, Transition, Initial)
        beta = backward(Observations, Emission, Transition, Initial)

        xi = np.zeros((N, N, T - 1))
        for t in range(T - 1):
            denominator = np.dot(
                alpha[:, t].T, Transition) @ (Emission[:, Observations[t + 1]] * beta[:, t + 1]) + 1e-8
            for i in range(N):
                numerator = alpha[i, t] * Transition[i, :] * \
                    Emission[:, Observations[t + 1]] * beta[:, t + 1]
                xi[i, :, t] = numerator / denominator

        gamma = np.sum(xi, axis=1)
        Transition_update = np.sum(xi, axis=2) / \
            (np.sum(gamma, axis=1)[:, None] + 1e-8)

        gamma = np.hstack(
            (gamma, np.sum(xi[:, :, T - 2], axis=0).reshape(-1, 1)))
        denominator = np.sum(gamma, axis=1) + 1e-8
        for s in range(M):
            Emission[:, s] = np.sum(
                gamma[:, Observations == s], axis=1) / denominator

        if np.allclose(Transition, Transition_update, atol=tol) and np.allclose(Emission, Emission, atol=tol):
            break
        Transition = Transition_update

    return Transition, Emission
