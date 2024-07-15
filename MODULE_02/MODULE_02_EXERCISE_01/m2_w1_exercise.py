# -*- coding: utf-8 -*-
"""M2_W1_Exercise.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1sbcm5upJDct8pSau0HikxBmgZkWt95PA

# Question 12
"""

# Download image
# !gdown 1i9dqan21DjQoG5Q_VEvm0LrVwAlXD0vB

import matplotlib.image as mpimg
import numpy as np
import pandas as pd


img = mpimg.imread('dog.jpeg')

gray_img_01 = (img.min(axis=2, keepdims=True) + img.max(axis=2, keepdims=True)) / 2
print(gray_img_01[0, 0])

"""# Question 13:"""

gray_img_02 = img.mean(axis=2, keepdims=True)
print(gray_img_02[0, 0])

"""# Question 14:"""

gray_img_03 = img[:, :, 0] * 0.21 + img[:, :, 1] * 0.72 + img[:, :, 2] * 0.07
print(gray_img_03[0, 0])

"""# Question 15:"""

# !gdown 1iA0WmVfW88HyJvTBSQDI5vesf-pgKabq

df = pd.read_csv('advertising.csv')

data = df.to_numpy()

max_index = data[:, [3]].argmax()
max_value = data[:, [3]][max_index][0]
print(f'Max value: {max_value}, Max index: {max_index}')

"""# Question 16:"""

tv_mean = data[:, [0]].mean()
print(f'Mean of TV column: {tv_mean}')

"""# Question 17:"""

sale_data = data[:, 3]
counts = len(sale_data[sale_data >= 20])
print(f'Count: {counts}')

"""# Question 18:"""

value = data[data[:, 3] >= 15][:, 1].mean()
print(f'Mean in Radio where Sales greater than 15: {value}')

"""# Question 19:"""

newspaper_mean = data[:, [2]].mean()
total = data[data[:, 2] > newspaper_mean][:, 3].sum()
print(f'Total Sales: {total}')

"""# Question 20:"""

sales_df = data[:, 3]
sales_mean = sales_df.mean()

scores = np.full(shape=sales_df.shape, fill_value="Good")

scores[sales_df > sales_mean] = "Good"
scores[sales_df == sales_mean] = "Average"

print(scores[7:10])