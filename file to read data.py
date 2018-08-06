# -*- coding: utf-8 -*-
"""
Created on Mon Aug  6 15:03:09 2018

@author: Ekansh Maheshwari
"""

from matplotlib import pyplot
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from mpl_toolkits.mplot3d import Axes3D
import re
df=pd.read_csv("data.csv")
#print(df)
df=df.drop(['Timestamp','Username'],axis=1)
#print(df.head())
print("LEngth of dataframe"+str(len(df)))    
print(type(df["Coding Languages you are proficient in:"][2]))
print(df["Coding Languages you are proficient in:"][2])
k=[]
m=[]
df = df[df["Number of Publications/Research Paper(If Any):"] != 999999999999999999999999]

for kz in range(0,len(df)):
    s=re.split(';|,| ; | , |; |\*|\n',df["Coding Languages you are proficient in:"][kz])
    for  j  in s:
        if j not in k :
            k.append(j)
            m.append(1)
        else:
            q=k.index(j)
            m[q]=m[q]+1
print(m)
print(k)
q=[]
z=[]
for kz in range(0,len(df)):
    #print(df["Number of Projects:"][kz])
    s=re.findall(r'\d+',df["Number of Projects:"][kz])
    if len(s)!=0:
        s=int(s[0])
    elif df["Number of Projects:"][kz] ==" One":
        s=1
        #print(s)
    else :
        s=1
    if s not in q:
        q.append(s)
        z.append(1) 
    else :
        ze=q.index(s)
        z[ze]=z[ze]+1
    '''s=int(re.findall(r'\d+',df["Number of Projects:"][kz]))
    if s not in q:
        q.append(s)
        z.append(1)
    else:
        le=k.index(s)
        z[le]=z[le]+1
    '''
print(q)
print(z)
papernumbers=[]
papernum=[]
kze="Number of Publications/Research Paper(If Any):"
for kz in range(0,len(df)):
    #s=re.findall(r'\d+',df["Number of Publications/Research Paper(If Any):"][kz])
    s=df["Number of Publications/Research Paper(If Any):"][kz]
    #if df["Number of Projects:"][kz]=="NA" or df["Number of Projects:"][kz]=="NA" or df["Number of Projects:"][kz]=="N/A" or df["Number of Projects:"][kz]=="None" or df["Number of Projects:"][kz]=="-" or df["Number of Projects:"][kz]=="." or df["Number of Projects:"][kz]=="N.A" or df["Number of Projects:"][kz]=="NO" or df["Number of Projects:"][kz]=="NA" or df["Number of Projects:"][kz]=="NONE" or df["Number of Projects:"][kz]=="Na" or df["Number of Projects:"][kz]=="Nil" or df["Number of Projects:"][kz]=="NA" or df["Number of Projects:"][kz]=="No it" or df["Number of Projects:"][kz]=="No publications/resarch paper" or df["Number of Projects:"][kz]=="NA" or df["Number of Projects:"][kz]=="No." or df["Number of Projects:"][kz]=="Nope" or df["Number of Projects:"][kz]=="Not yet" or df["Number of Projects:"][kz]=="Zero" or df["Number of Projects:"][kz]=="`NA" or df["Number of Projects:"][kz]=="no":
    #   s=0
    if type(s)!=float and s.isdigit() and int(s)>=0:
        s=int(s)
    elif s=='2':
        s=str(2)
    #elif s
    elif df[kze][kz]==" nan" or df[kze][kz]=="No" or df[kze][kz]=="NA" or df[kze][kz]=="NA" or df[kze][kz]=="N/A" or df[kze][kz]=="None" or df[kze][kz]=="-" or df[kze][kz]=="." or df[kze][kz]=="N.A" or df[kze][kz]=="NO" or df["Number of Projects:"][kz]=="NA" or df[kze][kz]=="NONE" or df[kze][kz]=="Na" or df[kze][kz]=="Nil" or df[kze][kz]=="NA" or df[kze][kz]=="No it" or df[kze][kz]=="No publications/resarch paper" or df[kze][kz]=="NA" or df[kze][kz]=="No." or df[kze][kz]=="Nope" or df[kze][kz]=="Not yet" or df[kze][kz]=="Zero" or df[kze][kz]=="`NA" or df[kze][kz]=="no":
        s=0
    elif df[kze][kz]=='"can plastic solar cell replace traditional silicon solar cell" in IEEE explore' or df[kze][kz]=="Soil stabilization ": 
        s=1
    
    else:
        mee= re.findall(r'\d+',df["Number of Projects:"][kz])
        if len(mee)!=0:
            s=int(mee[0])
        else:
            s=0
        print(df[kze][kz])
    #elif type(s)==str:
       #s=0
        print(df["Number of Projects:"][kz])
    if s not in papernumbers:     
        papernumbers.append(s)
        papernum.append(1)
    else:
        ze=papernumbers.index(s)
        papernum[ze]=papernum[ze]+1
print("oi")
print(papernum)
print(papernumbers)       
extraskilss=[]
extraskill=[]
for kz in range(0,len(df)):
    s=df[]