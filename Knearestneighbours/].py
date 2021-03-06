# -*- coding: utf-8 -*-
"""
Created on Mon Aug 13 19:01:32 2018

@author: Ekansh Maheshwari
"""

from sklearn import preprocessing, cross_validation
from sklearn.metrics import accuracy_score
import pandas as pd
#from sklearn import preprocessing
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor
import matplotlib as pl
colors=["","blue","green"]#blue=placed green =unplaced
df=pd.read_csv("new.csv")
df=df[df["cgpa"]<=10]
df=df[df["numberproject"]<=12]
df=df[df["numberevents"]<=12]
k=df[["numberenglishwritten","numberenglishspoken","numberquantativeaptitude","numbercompany"]]
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
ax.set_ylabel("Number of Project")
ax.set_zlabel("Number of Coding language")
ax.set_xticks([0,1,2,3,4])
ax.set_zticks([0,1,2,3,4,5])
z=[]
for i in range(0,11):
    z.append(i)
ax.set_yticks(z)
plt.show()
X_train,X_test,y_train,y_test=cross_validation.train_test_split(X,y,test_size=0.1)
model=RandomForestRegressor()
model.fit(X_train,y_train)
s=model.feature_importances_
print(model.feature_importances_)
for i in  range(0,len(s)):
    plt.bar(i,s[i])
#q=["numberinternship","numberevents","Number of Backlogs","numberenglishwritten","numberenglishspoken","numberquantativeaptitude","numberproject","numberbranch","cgpa","Number of Publications/Research Paper(If Any):","numberofcodinglanguage","numberextraskill"]
plt.show()
output = model.predict(X_test)
print(output)
for  i in range(0,len(output)):
    if output[i]>1.5:
        output[i]=2
    else:
        output[i]=1
print(output)
print(y_test)
se=accuracy_score(y_test,output)
print(se)
fig=plt.figure()
ax=fig.add_subplot(111,projection="3d")
for i in range(0,len(X_test)):
    #print(y[i])
    ax.scatter(X_test[i][0],X_test[i][1],X_test[i][2],color=colors[int(y_test[i])])
plt.show()
fig=plt.figure()
ax=fig.add_subplot(111,projection="3d")
x=[]
y=[]
ze=[]
for i in range(0,len(X_test)):
    #print(y[i])
    x.append(X_test[i][0])
    y.append(X_test[i][1])
    ze.append(X_test[i][2])
    ax.scatter(X_test[i][0],X_test[i][1],X_test[i][2],color=colors[int(output[i])])
x=max(x)
print(x)
y=max(y)
ze=max(ze)
xa=[]
ya=[]
za=[]
for i in range(0,int(x)+1):
    xa.append(i)
for i in range(1,int(y)+1):
    ya.append(i)
for i in range(1,int(ze)+1):
    za.append(i)
print(xa)
print(ya)
ax.set_xticks(xa)
ax.set_yticks(ya)
ax.set_zticks(za)
ax.set_xlabel("English Written")
ax.set_ylabel("English  Spoken")
ax.set_zlabel("Quantative Aptitude")
plt.show()