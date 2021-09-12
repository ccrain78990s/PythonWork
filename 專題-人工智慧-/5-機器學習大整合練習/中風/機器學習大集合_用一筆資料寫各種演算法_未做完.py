#!/usr/bin/env python
# -*- coding=utf-8 -*-
__author__ = "Chen"
"""
Stroke Prediction Dataset
資料來源
https://www.kaggle.com/fedesoriano/stroke-prediction-dataset

"""

"""
資料匯入&整理
"""
import pandas as pd
df=pd.read_csv('healthcare-dataset-stroke-data.csv')
print(df.head(5))
############
# 文字分類 轉 數字分類
df["gender"]=df.gender.astype("category").cat.codes                 #性別
df["ever_married"]=df.ever_married.astype("category").cat.codes
df["work_type"]=df.work_type.astype("category").cat.codes
df["Residence_type"]=df.Residence_type.astype("category").cat.codes
df["smoking_status"]=df.smoking_status.astype("category").cat.codes

#df.to_csv('中風.csv')
df2=df.dropna(axis=0, how='any')
#df2.to_csv('中風刪除有空值的資料.csv')


# 資料拆切
import numpy as np
from sklearn.model_selection import train_test_split

X= df2[['gender','age','hypertension','heart_disease','ever_married','work_type','Residence_type','avg_glucose_level','bmi','smoking_status']]
X=X.to_numpy()
Y= df2[['stroke']] # 2D
Y=Y.to_numpy()
t1=Y.shape[0]
Y=np.reshape(Y,(t1,))  # 2D 轉 1D

X_train , X_test , y_train , y_test = train_test_split(X,Y,test_size=0.2)


"""
import matplotlib.pyplot as plt
# seabron
# 畫seaborn圖
df111 = df2[['gender','age','hypertension','heart_disease','ever_married','work_type','Residence_type','avg_glucose_level','bmi','smoking_status','stroke']]
df222=df111[0:]
import seaborn as sns
sns.set_theme(style="ticks")
# df = sns.load_dataset("penguins")
sns.pairplot(df222,hue='stroke') #, hue="PM2.5")
#sns.pairplot(df2, hue="PM2.5")
plt.show()
"""



# KNN
print("**********===KNN===**********")
from sklearn.neighbors import KNeighborsClassifier  #KNN函式庫

# 演算法
knn = KNeighborsClassifier()
knn.fit(X_train, y_train)

print("預測",knn.predict(X_test))
print("實際",y_test)
print('準確率: %.2f' % knn.score(X_test, y_test))



# K-means
print("**********===K-means===**********")
from sklearn.cluster import KMeans
from sklearn import metrics

# 演算法
kmeans  = KMeans(n_clusters = 2)
kmeans.fit(X_train)
y_predict=kmeans.predict(X_train)

print("預測predict",kmeans.predict(X_test))
print("實際       ",y_test)
score = metrics.accuracy_score(y_test,kmeans.predict(X_test))
print('準確率:{0:f}'.format(score))


# 決策樹
print("**********===決策樹===**********")
from sklearn import tree

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
from sklearn.ensemble import RandomForestClassifier

# 演算法
RForest = RandomForestClassifier(n_estimators=100, max_depth=10,random_state=2)
RForest.fit(X, Y)

# tree.export_graphviz(clf,out_file='tree.dot')
print("預測答案:",RForest.predict(X_test))
print("實際答案:",y_test)
print('準確率: %.2f' % RForest.score(X_test, y_test))

# 貝氏分類器
print("**********===貝氏分類器===**********")

from sklearn.naive_bayes import GaussianNB

# 演算法
model = GaussianNB()
model.fit(X,Y)
#print(model.class_prior_ )
#print(model.get_params() )

#Predict Output
predicted= model.predict(X_test)
print(predicted)
print(model.predict_proba(X_test))


print("**********===PCA測試==**********")

from sklearn.decomposition import PCA
pca = PCA(n_components=3)
pca.fit(X)

print(pca.explained_variance_ratio_)

print(pca.singular_values_)

print("**********===SVR==**********")
from sklearn import svm

regr = svm.SVR()
regr.fit(X, Y)

print("預測答案:",regr.predict(X_test))
print("實際答案:",y_test)
print('準確率: %.2f' % regr.score(X_test, y_test))

print("**********===SGD==**********")
from sklearn.linear_model import SGDClassifier

clf = SGDClassifier(loss="hinge", penalty="l2", max_iter=5)
clf.fit(X, Y)

print("預測答案:",clf.predict(X_test))
print("實際答案:",y_test)
print('準確率: %.2f' % clf.score(X_test, y_test))