# -*- coding: utf-8 -*-
"""Untitlednewspaper1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1oyOWFzcGggdx09KyyMms_2e7yesFRIkd
"""

import pandas as pd

from google.colab import files
uploaded = files.upload()

df = pd.read_csv("IndianNewsPaper.csv")

df.head()

df.tail()

df.notnull()

print(df.isna().sum(axis = 0))

df.drop('Circulation', axis = 1,inplace = True)

df.nunique()

df['Format'].fillna(method='pad', inplace = True)

from sklearn.preprocessing import LabelEncoder,OneHotEncoder

le = LabelEncoder()
df['Format'] = le.fit_transform(df.Format)

df['Interval_of_publication'].unique()

le1 = LabelEncoder()
df['Interval_of_publication'] = le.fit_transform(df.Interval_of_publication)

df['Location'].fillna(method = 'pad', inplace = True)
df['Founded'].fillna(df['Founded'].mean().astype(int), inplace = True)

df.isnull().sum().sum()

df.head(100)



import matplotlib.pyplot as plt
 
 
fig = plt.figure()
ax = fig.add_axes([1,2,1,2])
ax.bar(df.Format,df.Interval_of_publication)
plt.show()

import numpy as np

x = np.linspace(df.Format, df.Interval_of_publication)
y = np.sinc(x)

fig, ax = plt.subplots()
ax.plot(x, y)
plt.show()