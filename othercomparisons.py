# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 00:24:00 2018

@author: Ekansh Maheshwari
"""
import pandas as pd
from sklearn import preprocessing, cross_validation
from sklearn.metrics import accuracy_score
import pandas as pd
#from sklearn import preprocessing
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor
import matplotlib as pl
df=pd.read_csv("new.csv")

k=df[df["numbercompany"]==1]
df=df[df["cgpa"]<=10]
df=df[df["numberproject"]<=12]
df=df[df["numberevents"]<=12]

s=0
#print(k)
k=k.reset_index()
for i in range(0,len(k)):
    #print(k["cgpa"][i])
    s=s+k["cgpa"][i]
s=s/len(k)
print("Average cgpa of placed people"+str(s))
'''s=0
#3print(k)
k=df[df["numbercompany"]==2]
k=k.reset_index()
#print(k)
s=0
for i in range(0,len(k)):
    #print(k["cgpa"][i])
    print(k["cgpa"][i])
    s=s+k["cgpa"][i]
#print(s)
s=s/len(k)
print("Average cgpa of unplaced people"+str(s))
'''
k=df[df["numbercompany"]==1 ]
k=k.reset_index()
print(k["Company Name(If placed and profile)"])
k["profile"]="Nothing"
a=["technical","informatica","kony","software","developer","(Risk","technology","analyst","odessa","novartis","nutanix","tek","bosch","vmware","robertbosch","risk","nissan","eag"]
b=["deloitte","sales","high","highradius","consulting"]
k["numberprofile"]=-3
for  i in range(0,len(k)):
    m=k["Company Name(If placed and profile)"][i]
    if type(m)==str:
        m=k["Company Name(If placed and profile)"][i].split(" ")
        for  j in m:
            if j.lower() in a:
                k["profile"][i]="Technical"   
                k["numberprofile"][i]=1

                break
            elif j.lower() in b:
                k["profile"][i]="Consultancy"
                k["numberprofile"][i]=2

                break
k=k[k["profile"]!="Nothing"]

print(k["profile"])
k=k.reset_index()
X=k[["numberinternship","numberevents","Number of Backlogs","numberenglishwritten","numberenglishspoken","numberquantativeaptitude","numberproject","cgpa","Number of Publications/Research Paper(If Any):","numberofcodinglanguage"]]
print(k)
y=k["numberprofile"]
print(str(len(X))+"X length")
X_train,X_test,y_train,y_test=cross_validation.train_test_split(X,y,test_size=0.1)
model=RandomForestRegressor()
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
plt.xlabel("The factors impacting selection in a developer or consultancy company")
plt.ylabel("Chances of selection in a type of company based on developer or consultancy")
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
for i in range(0,len(q)):
    print(str(s[i])+"   "+str(q[i]) )