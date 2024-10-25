#!/usr/bin/env python3
"""
Defines function that performs the Baum-Welch algorithm for Hidden Markov Model
"""

import numpy as np


def forward(Observations, Transition, Emission, Initial):
    T = Observations.shape[0]
    M = Transition.shape[0]
    F = np.zeros((M, T))

    # Initial step
    F[:, 0] = Initial.T * Emission[:, Observations[0]]

    # Recursive step
    for t in range(1, T):
        for j in range(M):
            F[j, t] = np.sum(F[:, t-1] * Transition[:, j]) * \
                Emission[j, Observations[t]]

    return F


def backward(Observations, Transition, Emission):
    T = Observations.shape[0]
    M = Transition.shape[0]
    B = np.zeros((M, T))

    # Initial step
    B[:, T-1] = 1

    # Recursive step
    for t in range(T - 2, -1, -1):
        for i in range(M):
            B[i, t] = np.sum(Transition[i, :] * Emission[:,
                             Observations[t+1]] * B[:, t+1])

    return B


def baum_welch(Observations, Transition, Emission, Initial, iterations=1000):
    T = Observations.shape[0]
    M = Transition.shape[0]
    N = Emission.shape[1]

    for n in range(iterations):
        # E-step: Forward and Backward calculations
        F = forward(Observations, Transition, Emission, Initial)
        B = backward(Observations, Transition, Emission)

        # Calculate gamma and xi
        gamma = np.zeros((M, T))
        xi = np.zeros((M, M, T - 1))

        for t in range(T - 1):
            denom = np.sum(F[:, t] * B[:, t])
            for i in range(M):
                gamma[i, t] = F[i, t] * B[i, t] / denom
                xi[i, :, t] = F[i, t] * Transition[i, :] * \
                    Emission[:, Observations[t+1]] * B[:, t+1] / denom

        # Last gamma for T-1
        gamma[:, T-1] = F[:, T-1] * B[:, T-1] / np.sum(F[:, T-1] * B[:, T-1])

        # M-step: Update Transition and Emission matrices
        Transition = np.sum(xi, axis=2) / \
            np.sum(gamma[:, :-1], axis=1).reshape((-1, 1))

        for j in range(N):
            mask = (Observations == j)
            Emission[:, j] = np.sum(
                gamma[:, mask], axis=1) / np.sum(gamma, axis=1)

    return Transition, Emission


# Example usage:
Observations = np.array([0, 1, 0, 2, 1])  # Example observation sequence
Transition = np.array([[0.7, 0.3], [0.4, 0.6]])  # Example transition matrix
Emission = np.array([[0.5, 0.4, 0.1], [0.1, 0.3, 0.6]]
                    )  # Example emission matrix
Initial = np.array([[0.6], [0.4]])  # Example initial probabilities

# Run Baum-Welch algorithm
Transition, Emission = baum_welch(
    Observations, Transition, Emission, Initial, iterations=10)

print("Updated Transition Matrix:")
print(np.round(Transition, 2))

print("Updated Emission Matrix:")
print(np.round(Emission, 2))
