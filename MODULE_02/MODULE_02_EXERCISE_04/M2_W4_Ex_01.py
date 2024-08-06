import numpy as np


def compute_mean(X):
    return np.mean(X, axis=0)


if __name__ == '__main__':
    X = [2, 0, 2, 2, 7, 4, -2, 5, -1, -1]

    print(f"Mean: {compute_mean(X)}")
