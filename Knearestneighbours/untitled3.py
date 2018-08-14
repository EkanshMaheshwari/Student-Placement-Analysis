# -*- coding: utf-8 -*-
"""
Created on Mon Aug 13 22:35:35 2018

@author: Ekansh Maheshwari
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Aug 12 22:09:10 2018

@author: Ekansh Maheshwari
"""
from numpy import genfromtxt
import pandas as pd
from sklearn import preprocessing, cross_validation,neighbors
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
colors=["","blue","green"]#blue=placed green =unplaced
df=pd.read_csv("new.csv")
print(df.head())
df=df[df["cgpa"]<=10]
df=df[df["numberproject"]<=12]
df=df[df["numberevents"]<=12]
print(df["numberevents"].max())
k=df[["cgpa","numberproject","numberofcodinglanguage","numbercompany"]]
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
ax.set_xlabel("CGPA")
ax.set_ylabel("Numbet of project")
ax.set_zlabel("Number of Coding languages")
ax.set_xticks([0,1,2,3,4])
ax.set_zticks([0,1,2,3,4,5])
z=[]
for i in range(0,11):
    z.append(i)
ax.set_yticks(z)
plt.show()
X_train,X_test,y_train,y_test=cross_validation.train_test_split(X,y,test_size=0.1)

X_train=genfromtxt("cgpaprojectcodinglanguagextrain.csv",delimiter=",")
X_test=genfromtxt("cgpaprojectcodinglanguagextest.csv",delimiter=",")
y_train=genfromtxt("cgpaprojectcodinglanguageytrain.csv",delimiter=",")
y_test=genfromtxt("cgpaprojectcodinglanguageytest.csv",delimiter=",")
print(X_test)
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
ax.set_xlabel("CGPA")
ax.set_ylabel("Numbet of project")
ax.set_zlabel("Number of Coding languages")

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
x=[]
y=[]
ze=[]
for i in range(0,len(X_test)):
    #print(y[i])
    x.append(X_test[i][0])
    y.append(X_test[i][1])
    ze.append(X_test[i][2])
    ay.scatter(X_test[i][0],X_test[i][1],X_test[i][2],color=colors[pred[i]])
print(x)
ay.set_xlabel("CGPA")
ay.set_ylabel("Numbet of project")
ay.set_zlabel("Number of Coding languages")
xa=[]
ya=[]
za=[]
for i in range(int(min(x)),int(max(x))+1):
    xa.append(i)
for i in range(int(min(y)),int(max(y))+1):
    ya.append(i)
for i in range(int(min(ze)),int(max(ze))+1):
    za.append(i)
print(xa)
print(ya)
ay.set_xticks(xa)
ay.set_yticks(ya)
ay.set_zticks(za)

plt.show()
#print(pred)
#print(y_test)

