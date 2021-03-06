# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1OFoz-jX_35tLC-jPRXlPfR4KYHPjdzwa
"""

#coding
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import chardet

dataset = pd.read_csv('2yvj9-uojkv.csv')
x = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values
print (x)
print (y)

from sklearn.impute import SimpleImputer
imputer = SimpleImputer(missing_values=np.nan, strategy='mean')
imputer.fit(x[:, 1:3])
x[:, 1:3] =imputer.transform(x[:, 1:3])

print (x)

from sklearn.compose import ColumTransformer
from sklearn.prepocessing import OneHotEncoder
ct = ColumTransformer(transformer=[('encoder', OneHotEncoder(), [0])], remaider='passthrough')
x = np.array(ct.fit_transform(x))

from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
y = le.fit_transform(y)

from sklearn.model_selection import train_test_split
x_train, x_text, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state =1)

print(x_train)

print(x_text)

print(y_train)

print(y_text)