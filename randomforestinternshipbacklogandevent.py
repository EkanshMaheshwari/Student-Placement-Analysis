# -*- coding: utf-8 -*-
"""
Created on Sat Aug 11 10:37:45 2018

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
k=df[["numberinternship","numberevents","Number of Backlogs","numberenglishwritten","numberenglishspoken","numberquantativeaptitude","numbercompany","numberproject","cgpa","Number of Publications/Research Paper(If Any):","numberofcodinglanguage"]]
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
model=RandomForestRegressor(100)
model.fit(X_train,y_train)
s=model.feature_importances_
print(model.feature_importances_)
q=["Number of internship","Number of events organized","Number of Backlogs","English written","English spoken","Quantative aptitude","Number of projects","CGPA","Number of research paper published","Number of coding language known"]
m=[]
for i in  range(0,len(s)):
    m.append(i)
plt.xticks(m ,q,rotation="vertical")
for i in  range(0,len(s)):
    plt.bar(i,s[i])
plt.xlabel("Factors Influencing Placement")
plt.ylabel("The impact on placement")
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
for i in range(0,len(X_test)):
    #print(y[i])
    ax.scatter(X_test[i][0],X_test[i][1],X_test[i][2],color=colors[int(output[i])])
plt.show()
for i in range(0,len(q)):
    print(str(s[i])+"   "+str(q[i]) )   