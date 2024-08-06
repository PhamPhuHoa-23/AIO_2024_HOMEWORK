import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


if __name__ == '__main__':
    data = pd.read_csv('advertising.csv')

    plt.figure(figsize=(10, 8))
    sns.heatmap(data.corr(), annot=True)
    plt.show()
