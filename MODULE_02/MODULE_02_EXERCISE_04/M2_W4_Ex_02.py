import numpy as np


def compute_median(X):
    X = np.sort(X)
    if len(X) % 2 == 1:
        return X[(len(X) + 1) // 2 - 1]
    else:
        return (X[len(X) // 2 - 1] + X[len(X) // 2]) / 2


if __name__ == '__main__':
    X = [1, 5, 4, 4, 9, 13]
    print(f"Median: {compute_median(X)}")
