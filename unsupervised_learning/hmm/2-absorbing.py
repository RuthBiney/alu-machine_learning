#!/usr/bin/env python3
'''
    function def absorbing(P): that
    determines if a markov chain is absorbing
'''

import numpy as np


def absorbing(P):
    '''
    Determines if a Markov chain is absorbing
    '''
    if (
        len(P.shape) != 2 or
        P.shape[0] != P.shape[1] or
        type(P) is not np.ndarray
    ):
        return None

    n = P.shape[0]
    D = np.diagonal(P)
    if (D == 1).all():
        return True
    if not (D == 1).any():
        return False

    # Find absorbing states
    absorbing_states = {i for i in range(n) if P[i, i] == 1}

    # Check if each non-absorbing state can lead to an absorbing state
    for i in range(n):
        if i not in absorbing_states:
            visited = set()
            queue = [i]
            found_absorbing = False

            while queue and not found_absorbing:
                state = queue.pop(0)
                if state in visited:
                    continue
                visited.add(state)

                for j in range(n):
                    if P[state, j] > 0:  # There is a transition
                        if j in absorbing_states:
                            found_absorbing = True
                            break
                        queue.append(j)

            if not found_absorbing:
                return False

    return True
