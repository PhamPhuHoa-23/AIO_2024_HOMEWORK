import pandas as pd
import numpy as np


if __name__ == '__main__':
    data = pd.read_csv('advertising.csv')
    
    x = data['Radio']
    y = data['Newspaper']

    result = np.corrcoef(x, y)
    print(result)