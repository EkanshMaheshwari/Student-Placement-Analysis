# -*- coding: utf-8 -*-
"""
Created on Fri Aug 10 13:38:54 2018

@author: Ekansh Maheshwari
"""

import pandas as pd
from sklearn import preprocessing, cross_validation,neighbors
import numpy as np
from  matplotlib import pyplot as plt

colors=["","blue","red"]#blue=placed green =unplaced
df=pd.read_csv("new.csv")
df=df[df["cgpa"]<=10]
df=df[df["numberproject"]<=12]
df=df[df["numberevents"]<=12]
k=df[["numbercompany","cgpa","numberproject"]]
print(k)
X=np.array(k.drop(["numbercompany"],1)) 
print(X)
y=np.array(k["numbercompany"])
for  i in range(0,len(X_train)):
    plt.scatter(X[i][1],X[i][0],color=colors[y_train[i]])
plt.show()

print(y)
X_train,X_test,y_train,y_test=cross_validation.train_test_split(X,y,test_size=0.1)
for  i in range(0,len(X_train)):
    plt.scatter(X_train[i][1],X_train[i][0],color=colors[y_train[i]])
plt.show()
clf=neighbors.KNeighborsClassifier()
clf.fit(X_train,y_train)
pred=clf.predict(X_train)
accuracy=clf.score(X_test,y_test)
print(pred)
i=0
print(X_test[0][0])
print(y_test[0])
print(len(X_test))
for i in range(0,len(X_test)):
    plt.scatter(X_test[i][1],X_test[i][0],color=colors[y_test[i]])
    print(i)
plt.show()
for i in range(0,len(X_test)):
    plt.scatter(X_test[i][1],X_test[i][0],color=colors[pred[i]])
    print(i)
print(accuracy)