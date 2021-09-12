#!/usr/bin/env python
# -*- coding=utf-8 -*-
__author__ = "Chen"
"""
Star Type Classification / NASA
資料來源
https://www.kaggle.com/brsdincer/star-type-classification


"""
"""
import pandas as pd
import matplotlib.pyplot as plt
# seabron
dataframe=pd.read_csv('Stars.csv')

# 畫seaborn 圖
df111 = dataframe[['Temperature','L','R','A_M','Color_type','Spectr2l_Cl2ss_type','Type']]
df222=df111[0:]
import seaborn as sns
sns.set_theme(style="ticks")
# df = sns.load_dataset("penguins")
sns.pairplot(df222,hue='Type') #, hue="PM2.5")
#sns.pairplot(df2, hue="PM2.5")
plt.show()
"""

# KNN
print("**********===KNN===**********")
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

# Load the diabetes dataset
#iris = datasets.load_iris()

import pandas as pd
df = pd.read_csv('Stars.csv')
#print(df.head())
#print(type(df))
X= df[['Temperature','L','R','A_M','Color_type','Spectr2l_Cl2ss_type']]
X=X.to_numpy()
Y= df[['Type']] # 2D
Y=Y.to_numpy()
t1=Y.shape[0]
Y=np.reshape(Y,(t1,))  # 2D 轉 1D

X_train , X_test , y_train , y_test = train_test_split(X,Y,test_size=0.2)

# 演算法
knn = KNeighborsClassifier()
knn.fit(X_train, y_train)

print("預測",knn.predict(X_test))
print("實際",y_test)
print('準確率: %.2f' % knn.score(X_test, y_test))



# K-means
print("**********===K-means===**********")
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.cluster import KMeans
from sklearn import metrics

# Load the diabetes dataset
df = pd.read_csv('Stars.csv')

X= df[['Temperature','L','R','A_M','Color_type','Spectr2l_Cl2ss_type']]
X=X.to_numpy()
Y= df[['Type']] # 2D
Y=Y.to_numpy()
t1=Y.shape[0]
Y=np.reshape(Y,(t1,))  # 2D 轉 1D

X_train , X_test , y_train , y_test = train_test_split(X,Y,test_size=0.2)

# 演算法
kmeans  = KMeans(n_clusters = 6)
kmeans.fit(X_train)
y_predict=kmeans.predict(X_train)

print("預測predict",kmeans.predict(X_test))
print("實際       ",y_test)
#print("預測",kmeans_fit.labels_)
score = metrics.accuracy_score(y_test,kmeans.predict(X_test))
print('準確率:{0:f}'.format(score))

"""
x1=df_X_train[:, 0]
y1=df_X_train[:, 1]
plt.scatter(x1,y1, c=y_predict, cmap='viridis')

centers = kmeans.cluster_centers_
plt.scatter(centers[:, 0], centers[:, 1], c='black', s=200, alpha=0.5);
plt.show()
"""


# 決策樹
print("**********===決策樹===**********")
import numpy as np
from sklearn import tree

import pandas as pd
df = pd.read_csv('Stars.csv')

X= df[['Temperature','L','R','A_M','Color_type','Spectr2l_Cl2ss_type']]
X=X.to_numpy()
Y= df[['Type']] # 2D
Y=Y.to_numpy()
t1=Y.shape[0]
Y=np.reshape(Y,(t1,))  # 2D 轉 1D

X_train , X_test , y_train , y_test = train_test_split(X,Y,test_size=0.2)

# 演算法
clf = tree.DecisionTreeClassifier()
clf = clf.fit(X_train,y_train)

# tree.export_graphviz(clf,out_file='tree.dot')
print("預測答案:",clf.predict(X_test))
print("實際答案:",y_test)
print('準確率: %.2f' % clf.score(X_test, y_test))
#import matplotlib.pyplot as plt
#tree.plot_tree(clf)
#plt.show()


# Regression 沒做 不合適 找別的資料做吧~~~~

# 隨機森林
print("**********===隨機森林===**********")
import numpy as np
from sklearn.ensemble import RandomForestClassifier

import pandas as pd
df = pd.read_csv('Stars.csv')

X= df[['Temperature','L','R','A_M','Color_type','Spectr2l_Cl2ss_type']]
X=X.to_numpy()
Y= df[['Type']] # 2D
Y=Y.to_numpy()
t1=Y.shape[0]
Y=np.reshape(Y,(t1,))  # 2D 轉 1D

X_train , X_test , y_train , y_test = train_test_split(X,Y,test_size=0.2)

# 演算法
RForest = RandomForestClassifier(n_estimators=100, max_depth=10,
                             random_state=2)
RForest.fit(X, Y)
#print(RForest.predict([[180, 85]]))
#print(RForest.predict([[163, 65]]))

# tree.export_graphviz(clf,out_file='tree.dot')
print("預測答案:",RForest.predict(X_test))
print("實際答案:",y_test)
print('準確率: %.2f' % RForest.score(X_test, y_test))



# 貝氏分類器
print("**********===貝氏分類器===**********")
import numpy as np
from sklearn.naive_bayes import GaussianNB

import pandas as pd
df = pd.read_csv('Stars.csv')

X= df[['Temperature','L','R','A_M','Color_type','Spectr2l_Cl2ss_type']]
X=X.to_numpy()
Y= df[['Type']] # 2D
Y=Y.to_numpy()
t1=Y.shape[0]
Y=np.reshape(Y,(t1,))  # 2D 轉 1D

X_train , X_test , y_train , y_test = train_test_split(X,Y,test_size=0.2)

# 演算法
model = GaussianNB()
model.fit(X,Y)
#print(model.class_prior_ )
#print(model.get_params() )

#Predict Output
predicted= model.predict(X_test)
print(predicted)
print(model.predict_proba(X_test))




