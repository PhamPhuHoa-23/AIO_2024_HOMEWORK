import pandas as pd
from M2_W4_Ex_05 import correlation


if __name__ == '__main__':
    data = pd.read_csv('advertising.csv')

    features = ['TV', 'Radio', 'Newspaper']

    for feature_1 in features:
        for feature_2 in features:
            correlation_value = correlation(data[feature_1], data[feature_2])
            print(f'Correlation between {feature_1} and {feature_2}: {round(correlation_value, 2)}')
