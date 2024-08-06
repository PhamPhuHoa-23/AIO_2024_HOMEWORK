import numpy as np
from M2_W4_Ex_01 import compute_mean
from M2_W4_Ex_03 import compute_std


def compute_correlation_cofficient(X, Y):
    x, y = np.array(X), np.array(Y)
    xy = X * Y

    mean_x = compute_mean(x)
    mean_y = compute_mean(y)
    mean_xy = compute_mean(xy)

    std_x = compute_std(x)
    std_y = compute_std(y)

    numerator = mean_xy - mean_x * mean_y
    denominator = std_x * std_y

    return numerator / denominator


if __name__ == '__main__':
    X = np.asarray([-2, -5, -11, 6, 4, 15, 9])
    Y = np.asarray([4, 25, 121, 35, 16, 225, 81])
    print(f"Correlation cofficient: {compute_correlation_cofficient(X, Y)}")
