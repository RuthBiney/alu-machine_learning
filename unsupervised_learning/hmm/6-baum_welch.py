#!/usr/bin/env python3
"""
Defines function that performs the Baum-Welch algorithm for Hidden Markov Model
"""

import numpy as np


def forward(Observations, Transition, Emission, Initial):
    """
    Performs the forward algorithm for a hidden Markov model (HMM).

    Parameters:
    - Observations (numpy.ndarray): Shape (T,), index of the observations where T is the number of observations.
    - Transition (numpy.ndarray): Shape (M, M), transition probability matrix where M is the number of hidden states.
    - Emission (numpy.ndarray): Shape (M, N), emission probability matrix where N is the number of observation states.
    - Initial (numpy.ndarray): Shape (M, 1), initial probability vector.

    Returns:
    - alpha (numpy.ndarray): Shape (T, M), the forward probabilities matrix.
    """
    T = Observations.shape[0]
    M = Transition.shape[0]
    alpha = np.zeros((T, M))

    # Initialize alpha at time 0
    alpha[0, :] = Initial.T * Emission[:, Observations[0]]

    # Compute alpha for each time step t
    for t in range(1, T):
        for j in range(M):
            alpha[t, j] = np.sum(
                alpha[t - 1, :] * Transition[:, j]) * Emission[j, Observations[t]]

    return alpha


def backward(Observations, Transition, Emission):
    """
    Performs the backward algorithm for a hidden Markov model (HMM).

    Parameters:
    - Observations (numpy.ndarray): Shape (T,), index of the observations where T is the number of observations.
    - Transition (numpy.ndarray): Shape (M, M), transition probability matrix where M is the number of hidden states.
    - Emission (numpy.ndarray): Shape (M, N), emission probability matrix where N is the number of observation states.

    Returns:
    - beta (numpy.ndarray): Shape (T, M), the backward probabilities matrix.
    """
    T = Observations.shape[0]
    M = Transition.shape[0]
    beta = np.zeros((T, M))

    # Initialize beta at time T - 1
    beta[T - 1, :] = 1

    # Compute beta for each time step t
    for t in range(T - 2, -1, -1):
        for i in range(M):
            beta[t, i] = np.sum(beta[t + 1, :] * Transition[i, :]
                                * Emission[:, Observations[t + 1]])

    return beta


def baum_welch(Observations, Transition, Emission, Initial, iterations=1000, tol=1e-6):
    """
    Performs the Baum-Welch algorithm (an instance of the Expectation-Maximization algorithm) for a hidden Markov model (HMM).

    Parameters:
    - Observations (numpy.ndarray): Shape (T,), index of the observations where T is the number of observations.
    - Transition (numpy.ndarray): Shape (M, M), initial transition probability matrix where M is the number of hidden states.
    - Emission (numpy.ndarray): Shape (M, N), initial emission probability matrix where N is the number of observation states.
    - Initial (numpy.ndarray): Shape (M, 1), initial state distribution.
    - iterations (int, optional): The number of iterations of the expectation-maximization process to perform. Default is 1000.
    - tol (float, optional): The tolerance level for convergence. Default is 1e-6.

    Returns:
    - Transition (numpy.ndarray): The updated transition probability matrix.
    - Emission (numpy.ndarray): The updated emission probability matrix.
    """
    T = Observations.shape[0]
    M = Transition.shape[0]
    N = Emission.shape[1]

    for iteration in range(iterations):
        # Save previous values for convergence check
        prev_Transition = np.copy(Transition)
        prev_Emission = np.copy(Emission)

        # Expectation step (E-step)
        alpha = forward(Observations, Transition, Emission, Initial)
        beta = backward(Observations, Transition, Emission)

        # Initialize xi and gamma
        xi = np.zeros((T - 1, M, M))
        gamma = np.zeros((T, M))

        # Compute xi and gamma
        for t in range(T - 1):
            denominator = np.sum(np.outer(
                alpha[t, :], beta[t + 1, :]) * Transition * Emission[:, Observations[t + 1]])
            for i in range(M):
                numerator = alpha[t, i] * Transition[i, :] * \
                    Emission[:, Observations[t + 1]] * beta[t + 1, :]
                xi[t, i, :] = numerator / denominator

        # Sum over xi to get gamma
        gamma = np.sum(xi, axis=2)

        # Include the last time step in gamma
        gamma = np.vstack((gamma, np.sum(xi[T - 2, :, :], axis=0)))

        # Maximization step (M-step)
        # Update Transition matrix
        Transition = np.sum(xi, axis=0) / \
            np.sum(gamma[:-1], axis=0).reshape((-1, 1))

        # Update Emission matrix
        for i in range(M):
            for k in range(N):
                relevant_observations = (Observations == k).astype(int)
                Emission[i, k] = np.sum(
                    gamma[:, i] * relevant_observations) / np.sum(gamma[:, i])

        # Ensure the transition and emission probabilities are normalized
        Transition = Transition / np.sum(Transition, axis=1, keepdims=True)
        Emission = Emission / np.sum(Emission, axis=1, keepdims=True)

        # Check for convergence
        if np.allclose(Transition, prev_Transition, atol=tol) and np.allclose(Emission, prev_Emission, atol=tol):
            print(f"Converged after {iteration + 1} iterations")
            break

    return Transition, Emission
