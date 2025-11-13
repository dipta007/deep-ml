import numpy as np


def linear_regression_gradient_descent(X: np.ndarray, y: np.ndarray, alpha: float, iterations: int) -> np.ndarray:
    # Your code here, make sure to round
    m, n = X.shape
    theta = np.zeros((n, 1))
    return theta


if __name__ == "__main__":
    X = np.array([[1, 2, 3], [4, 5, 6]])
    y = np.array([1, 2, 3])
    alpha = 0.01
    iterations = 1000
    print(linear_regression_gradient_descent(X, y, alpha, iterations))
