# -*- coding: utf-8 -*-
"""
Created on Fri Aug 10 19:54:22 2018

@author: Ekansh Maheshwari
"""
import pandas as pd
from sklearn import preprocessing, cross_validation,neighbors
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
colors=["","blue","green"]#blue=placed green =unplaced
df=pd.read_csv("new.csv")
df=df[df["cgpa"]<=10]
df=df[df["numberproject"]<=12]
df=df[df["numberevents"]<=12]
print(df["numberevents"].max())
k=df[["numberinternship","numberevents","Number of Backlogs","numbercompany"]]
X=np.array(k.drop(["numbercompany"],1)) 
#print(X)
y=np.array(k["numbercompany"])
fig=plt.figure()
ax=fig.add_subplot(111,projection="3d")
#print(X)
#print(y)
#print(X[3])
for i in range(0,len(X)):
    #print(y[i])
    ax.scatter(X[i][0],X[i][1],X[i][2],color=colors[y[i]])
ax.set_xlabel("number of intership")
ax.set_ylabel("Number of event")
ax.set_zlabel("Number of backlog")
ax.set_xticks([0,1,2,3,4])
ax.set_zticks([0,1,2,3,4,5])
z=[]
for i in range(0,11):
    z.append(i)
ax.set_yticks(z)
plt.show()
X_train,X_test,y_train,y_test=cross_validation.train_test_split(X,y,test_size=0.1)
clf=neighbors.KNeighborsClassifier()
clf.fit(X_train,y_train)
pred=clf.predict(X_test)
accuracy=clf.score(X_test,y_test)
print(accuracy)
fig=plt.figure()
ay=fig.add_subplot(111,projection="3d")

for i in range(0,len(X_train)):
    #print(y[i])
    ay.scatter(X_train[i][0],X_train[i][1],X_train[i][2],color=colors[y_train[i]])
ay.set_xlabel("number of intership")
ay.set_ylabel("Number of event")
ay.set_zlabel("Number of backlog")
ay.set_xticks([0,1,2,3,4])
ay.set_zticks([0,1,2,3,4,5])
plt.show()
print(accuracy)
fig=plt.figure()
ay=fig.add_subplot(111,projection="3d")

for i in range(0,len(X_test)):
    #print(y[i])
    ay.scatter(X_test[i][0],X_test[i][1],X_test[i][2],color=colors[y_test[i]])
plt.show()
fig=plt.figure()
ay=fig.add_subplot(111,projection="3d")

for i in range(0,len(X_test)):
    #print(y[i])
    ay.scatter(X_test[i][0],X_test[i][1],X_test[i][2],color=colors[pred[i]])

ay.set_xlabel("number of intership")
ay.set_ylabel("Number of event")
ay.set_zlabel("Number of backlog")
ay.set_xticks([0,1,2,3,4])
ay.set_zticks([0,1,2,3,4,5])
plt.show()
print(pred)
print(y_test)