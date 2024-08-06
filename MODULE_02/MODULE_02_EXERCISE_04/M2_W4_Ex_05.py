import numpy as np
import pandas as pd
from M2_W4_Ex_01 import compute_mean
from M2_W4_Ex_03 import compute_std

def correlation(x, y):
    x = x.to_numpy()
    y = y.to_numpy()

    xy = x * y

    mean_x = compute_mean(x)
    mean_y = compute_mean(y)
    mean_xy = compute_mean(xy)

    std_x = compute_std(x)
    std_y = compute_std(y)

    numerator = mean_xy - mean_x * mean_y
    denominator = std_x * std_y

    return numerator / denominator


if __name__ == '__main__':
    data = pd.read_csv("advertising.csv")

    x = data['TV']
    y = data['Radio']

    print(f"Correlation between TV and Radio: {correlation(x, y)}")
