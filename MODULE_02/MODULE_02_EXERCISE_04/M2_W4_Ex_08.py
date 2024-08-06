import pandas as pd


if __name__ == '__main__':
    data = pd.read_csv('advertising.csv')

    print(data.corr())
    