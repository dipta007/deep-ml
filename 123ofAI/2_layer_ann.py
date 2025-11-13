import numpy as np


def relu(x):
    return np.maximum(np.zeros_like(x), x)


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def forward_pass(x, W1, b1, W2, b2):
    x = np.asarray(x, dtype=float)
    W1 = np.asarray(W1, dtype=float)
    b1 = np.asarray(b1, dtype=float)
    W2 = np.asarray(W2, dtype=float)
    b2 = np.asarray(b2, dtype=float)

    y = W1 @ x + b1
    y = relu(y)
    y = W2 @ y + b2
    y = sigmoid(y)

    return np.round(y, 2).item()


if __name__ == "__main__":
    # [1.0, 1.0], [[0.1, 0.2], [0.3, 0.1], [0.0, 0.5], [0.4, 0.2]], [0.1, 0.0, 0.1, 0.0], [[0.3, 0.2, 0.1, 0.4]], 0.0
    x = [1.0, 1.0]
    W1 = [[0.1, 0.2], [0.3, 0.1], [0.0, 0.5], [0.4, 0.2]]
    b1 = [0.1, 0.0, 0.1, 0.0]
    W2 = [[0.3, 0.2, 0.1, 0.4]]
    b2 = 0.0
    print(forward_pass(x, W1, b1, W2, b2))
