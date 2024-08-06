import numpy as np
from M2_W4_Ex_01 import compute_mean


def compute_std(X):
    mean = compute_mean(X)
    variance = 0

    for x in X:
        variance += (x - mean) ** 2

    return np.sqrt(variance / len(X))


if __name__ == '__main__':
    X = [171, 176, 155, 167, 169, 182]
    compute_std(X)
