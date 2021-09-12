#!/usr/bin/env python
# -*- coding=utf-8 -*-
__author__ = "Chen"
# KNN heart 心臟病發生可能性(target:0=少機率 1=多機率)
"""
資料來源:
https://www.kaggle.com/nareshbhat/health-care-data-set-on-heart-attack-possibility


"""

import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

# Load the diabetes dataset
#iris = datasets.load_iris()

import pandas as pd
df = pd.read_csv('heart.csv')
print(df.head())
print(type(df))
X= df[['age','sex','cp','trestbps','chol','fbs','restecg','thalach','exang','oldpeak','slope','ca','thal']]
X=X.to_numpy()
Y= df[['target']] # 2D
Y=Y.to_numpy()
t1=Y.shape[0]
Y=np.reshape(Y,(t1,))  # 2D 轉 1D


#iris_X_train , iris_X_test , iris_y_train , iris_y_test = train_test_split(df[["","","",""]],df[""],test_size=0.2)
X_train , X_test , y_train , y_test = train_test_split(X,Y,test_size=0.2)
knn = KNeighborsClassifier()
knn.fit(X_train, y_train)

print("預測",knn.predict(X_test))
print("實際",y_test)
print('準確率: %.2f' % knn.score(X_test, y_test))
