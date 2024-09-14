import numpy as np

def bi_rnn(bi_cell, X, h_0, h_T):
    '''
        Function that performs forward propagation for a bidirectional RNN

        parameters:
            bi_cell: an instance of BidirectionalCell
            X: data input of shape (t, m, i)
            h_0: initial hidden state of shape (m, h)
            h_T: terminal hidden state of shape (m, h)

        return:
            H: all hidden states
            Y: all outputs
    '''

    t, m, i = X.shape  # t = time steps, m = batch size, i = input size
    h = h_0.shape[1]   # h = hidden state size

    # Initialize H with zeros: (t + 1, 2, m, h) -> t+1 time steps, 2 directions, batch size, hidden size
    H = np.zeros((t + 1, 2, m, h))

    # Set the initial hidden states for both directions
    H[0, 0] = h_0  # Forward direction
    H[-1, 1] = h_T  # Backward direction

    # Forward direction (left to right)
    for step in range(t):
        H[step + 1, 0] = bi_cell.forward(H[step, 0], X[step])

    # Backward direction (right to left)
    for step in reversed(range(t)):
        H[step, 1] = bi_cell.backward(H[step + 1, 1], X[step])

    # Outputs for all time steps
    Y = bi_cell.output(H[1:, 0], H[:-1, 1])

    return H, Y
