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

df=pd.read_csv("dat.csv")
#df = df.drop_duplicates('Username')
#print(df)
df=df.drop(['Timestamp','Username'],axis=1)
#print(df.head())

print("LEngth of dataframe"+str(len(df)))    

print(type(df["Coding Languages you are proficient in:"][2]))
print(df["Coding Languages you are proficient in:"][2])
k=[]
m=[]
df = df[df["Number of Publications/Research Paper(If Any):"] != 999999999999999999999999]
df["numberofcodinglanguage"]=-10
for kz in range(0,len(df)):
    i=0
    s=re.split(';|,| ; | , |; |\*|\n',df["Coding Languages you are proficient in:"][kz])
    for  j  in s:
        if j not in k :
            i=i+1
            k.append(j)
            m.append(1)
        else:
            i=i+1
            q=k.index(j)
            m[q]=m[q]+1
    df["numberofcodinglanguage"][kz]=i
print(m)
print(k)

q=[]
z=[]
df["numberproject"]=-23
for kz in range(0,len(df)):
    #print(df["Number of Projects:"][kz])
    if type(df["Number of Projects:"][kz])==str:
        s=re.findall(r'\d+',df["Number of Projects:"][kz])
        if len(s)!=0:
            s=int(s[0])
            df["numberproject"][kz]=s
        elif df["Number of Projects:"][kz] ==" One":
            s=1
            df["numberproject"][kz]=s
            #print(s)
        else :
            s=1
            df["numberproject"][kz]=s
        if s not in q:
            q.append(s)
            z.append(1) 
        else :
            ze=q.index(s)
            z[ze]=z[ze]+1
    elif str.isdigit(str(df["Number of Projects:"][kz]))==True:
        s=int(df["Number of Projects:"][kz])
        df["numberproject"][kz]=s
    else:
        df["numberproject"][kz]=0
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
extraskills=[]
extraskill=[]
df["numberextraskill"]=0
for kz in range(0,len(df)):
    j=0
    s=re.split(';|,| ; | , |; |\*|\n|and|AND|/|&',str(df["Any Extra/Other Skills:"][kz]))
    for i in s:
        if len(i)>0 and i[0]==" ":
            i=i[1:]
        if len(i)>0 and i[-1]==" ":
            i=i[0:-1]
        if str.upper(i)=="INTERNET OF THINGS" or str.upper(i)=="INTERNET OF THINGS (IOT)" or str.upper(i)=="INTERNET OF THINGS.":
            i="IOT"
        if str.upper(i)=="PLC TRAINING":
            i="PLC"
          
        if str.upper(i)=="CC":
            i="CLOUD COMPUTING"
            
        if str.upper(i)=="HACKING":
            i="ETHICAL HACKING"
            
        if str.upper(i)=="EMBEDDED":
            i="EMBEDDED SYSTEMS"
            
        if str.upper(i)=="BASIC ROBOTICS.":
            i= "ROBOTICS"
            
        if str.upper(i)==" PHOTOSHOP":
            i="PHOTOSHOP"
        
        if str.upper(i) not in extraskills and i!=" " and str.upper(i)!="NAN" and str.upper(i)!="NO" and str.upper(i)!="N" and str.upper(i)!="NOTHING" and str.upper(i)!="" and str.upper(i)!="NONE": 
            extraskills.append(str.upper(i))
            extraskill.append(1)
            
            j=j+1
        elif  i!=" " and str.upper(i)!="NAN" and str.upper(i)!="NO" and str.upper(i)!="N" and str.upper(i)!="NOTHING" and str.upper(i)!="" and str.upper(i)!="NONE":
            ze=extraskills.index(str.upper(i))
            extraskill[ze]=extraskill[ze]+1
            j=j+1
    df["numberextraskill"][kz]=j
print(extraskills)
print(extraskill)

df["numberinternship"]=-12
internship=[]
internships=[]
m=["Nil","Na","No internships only Industrial trainings.","No","None","nil","N/A"]
for kz in range(0,len(df)):
    if type(df["Internship Experience (The number of internship  and company name):"][kz])==str:
        s=re.findall('\d+',df["Internship Experience (The number of internship  and company name):"][kz])
        if len(s)!=0:
             #print(s[-1])    
             if int(s[-1])  not in internship:
                 df["numberinternship"][kz]=int(s[-1])
                 internship.append(int(s[-1]))
                 internships.append(1)
             else:
                df["numberinternship"][kz]=int(s[-1])
                ze=internship.index(int(s[-1]))
                internships[ze]=internships[ze]+1
        elif len(s)==0:    
            lq=df["Internship Experience (The number of internship  and company name):"][kz].count(",")
            if lq>0:
                if lq+1 not in internship:
                    df["numberinternship"][kz]=lq+1
                    internship.append(lq+1)
                    internships.append(1)
                else:
                    df["numberinternship"][kz]=lq+1
                    ze=internship.index(lq+1)
                    internships[ze]=internships[ze]+1
            elif df["Internship Experience (The number of internship  and company name):"][kz] in m:
                q=0
                if q not in internship:
                    df["numberinternship"][kz]=q  
                    internship.append(q)
                    internships.append(1)
                else:
                    df["numberinternship"][kz]=q
                    ze=internship.index(q)
                    internships[ze]=internships[ze]+1
            else:
                q=1
                if q not in internship:
                    df["numberinternship"][kz]=q
                    internship.append(q)
                    internships.append(1)
                else:
                    df["numberinternship"][kz]=q
                    ze=internship.index(q)
                    internships[ze]=internships[ze]+1
                
        '''if df["Internship Experience (The number of internship  and company name):"][kz] not in internship:
            internship.append(df["Internship Experience (The number of internship  and company name):"][kz])
            internships.append(1)
        else:
            ze=internship.index(df["Internship Experience (The number of internship  and company name):"][kz])
            internship[ze]=internship[ze]+1
        '''
    else:
        q=0
        if q not in internship:
                    df["numberinternship"][kz]=q
                    internship.append(q)
                    internships.append(1)
        else:
                    df["numberinternship"][kz]=q
                    ze=internship.index(q)
                    internships[ze]=internships[ze]+1
                
        #print(df["Internship Experience (The number of internship  and company name):"][kz])
print("No of internship")
print(internship)
print(internships)

event=[]
events=[]
count=0

kze="Events Organised:"
df["numberevents"]=-23
for i in range(0,len(df)):
    if type(df["Events Organised:"][i])==str and str.isdigit(df["Events Organised:"][i])==False:
        s=re.findall('\d+',df["Events Organised:"][i])
        if len(s)!=0 :
             #print(s[-1])    
             if int(s[-1])  not in event and int(s[-1])<=12:
                 event.append(int(s[-1]))
                 df["numberevents"][i]=int(s[-1])
                 events.append(1)
             elif int(s[-1])<=12:
                 df["numberevents"][i]=int(s[-1])
                 ze=event.index(int(s[-1]))
                 events[ze]=events[ze]+1
             else:
                #if df["Events Organised:"][i]=="•Coordinator of Kreative eye (2018)- The official photography society of KIIT. •Member of the broadcasting team of KIIT MUN 2016, 2017. •Member of the organizing committee of KIITFEST, the annual cultural fest of KIIT. •Member of the organizing committee of TEDxKIIT University 2017.":
                    
                if df["Events Organised:"][i].count(",")>0:
                    #print(df["Events Organised:"][i])
                    q=df["Events Organised:"][i].count(",")+1
                    #print(q)
                    if q not in event:
                        df["numberevents"][i]=q
                        event.append(q)
                        events.append(1)
                    else:
                        df["numberevents"][i]=q
                        ze=event.index(q)
                        events[ze]=events[ze]+1
                else :
                    q=1
                    if q not in event:
                        df["numberevents"][i]=q
                        event.append(q)
                        events.append(1)
                    else:
                        df["numberevents"][i]=q
                        ze=event.index(q)
                        events[ze]=events[ze]+1
                    print(df["Events Organised:"][i])
        elif df["Events Organised:"][i].count(",")>0 and df["Events Organised:"][i]!="None. ðŸ˜‚ ":
            q=df["Events Organised:"][i].count(",")+1
            #print(q)
            if q not in event:
                df["numberevents"][i]=q
                event.append(q)
                events.append(1)
            else:
                df["numberevents"][i]=q
                ze=event.index(q)
                events[ze]=events[ze]+1
        elif str.upper(df["Events Organised:"][i])=="NONE" or  str.upper(df["Events Organised:"][i])=="NO" or str.upper(df["Events Organised:"][i])=="NA" or str.upper(df["Events Organised:"][i])=="NONE." or str.upper(df["Events Organised:"][i])=="NIL" or df["Events Organised:"][i]=="No events organised. " or df["Events Organised:"][i]=="No event ":
            q=0
            if q not in event:
                        df["numberevents"][i]=q
                        event.append(q)
                        events.append(1)
            else:
                        df["numberevents"][i]=q
                        ze=event.index(q)
                        events[ze]=events[ze]+1
        else:
            #print(df["Events Organised:"][i])
            q=1
            if q not in event:
                        df["numberevents"][i]=q
                        event.append(q)
                        events.append(1)
            else:
                        df["numberevents"][i]=q
                        ze=event.index(q)
                        events[ze]=events[ze]+1
            
    elif type(df["Events Organised:"][i])==str and str.isdigit(df["Events Organised:"][i]) :
              #print(df["Events Organised:"][i])
              q=int(df["Events Organised:"][i])
              if q not in event:
                        df["numberevents"][i]=q
                        event.append(q)
                        events.append(1)
              else:
                        df["numberevents"][i]=q
                        ze=event.index(q)
                        events[ze]=events[ze]+1   
    else:
        q=0
        if q not in event:
                        df["numberevents"][i]=q
                        event.append(q)
                        events.append(1)
        else:
                        df["numberevents"][i]=q
                        ze=event.index(q)
                        events[ze]=events[ze]+1
        
        #print(df["Events Organised:"][i])
        #elif len(s)==0:
        #print(df["Events Organised:"][i])
    
print(event)
print(events)
print(count)
print(df["numberevents"])
lbmake=LabelEncoder()
df["numberbranch"]=lbmake.fit_transform(df["Branch"])+1
#print(df["numberbranch"].head())
#print(df["Branch"].head())
print(df[df["numberbranch"]==3])#Mech=7 CSE=2 IT=6 CIVIL=1 EE=4 EEE=5 E&I=3
df["numberenglishwritten"]=-2
#lbmake=LabelEncoder()
for i in range(0,len(df)):
    if df["English Written:"][i]=="Bad":
        df["numberenglishwritten"][i]=1
    elif df["English Written:"][i]=="Average":
        df["numberenglishwritten"][i]=2
    elif df["English Written:"][i]=="Good":
        df["numberenglishwritten"][i]=3
    elif df["English Written:"][i]=="Very Good":
        df["numberenglishwritten"][i]=4
    elif df["English Written:"][i]=="Excellent":
        df["numberenglishwritten"][i]=5
df["numberenglishspoken"]=-2 
for i in range(0,len(df)):
    if df["English Spoken:"][i]=="Bad":
        df["numberenglishspoken"][i]=1
    elif df["English Spoken:"][i]=="Average":
        df["numberenglishspoken"][i]=2
    elif df["English Spoken:"][i]=="Good":
        df["numberenglishspoken"][i]=3
    elif df["English Spoken:"][i]=="Very Good":
        df["numberenglishspoken"][i]=4
    elif df["English Spoken:"][i]=="Excellent":
        df["numberenglishspoken"][i]=5
    
    
    
#df["numberenglishwritten"]=lbmake.fit_transform(df["English Written:"])+1
#print(df[df["numberenglishwritten"]==5].head())#Average=1 Bad=2 Excellent=3 GOOD=4 VERY GOOD=5
'''lbmake=LabelEncoder()
df["numberenglishspoken"]=lbmake.fit_transform(df["English Spoken:"])+1
s=df[df["English Spoken:"]=="Average"].head()#Average=1 Bad=2 Excellent=3 GOOD=4 VERY GOOD=5

print(s[["English Spoken:","numberenglishspoken"]])
'''
df["numberquantativeaptitude"]=2 
for i in range(0,len(df)):
    if df["Quantitative Aptitude:"][i]=="Bad":
        df["numberquantativeaptitude"][i]=1
    elif df["Quantitative Aptitude:"][i]=="Average":
        df["numberenglishspoken"][i]=2
    elif df["Quantitative Aptitude:"][i]=="Good":
        df["numberquantativeaptitude"][i]=3
    elif df["Quantitative Aptitude:"][i]=="Very Good":
        df["numberquantativeaptitude"][i]=4
    elif df["Quantitative Aptitude:"][i]=="Excellent":
        df["numberquantativeaptitude"][i]=5

'''lbmake=LabelEncoder()
df["numberquantativeaptitude"]=lbmake.fit_transform(df["Quantitative Aptitude:"])+1
s=df[df["Quantitative Aptitude:"]=="Very Good"].head()#Average=1 Bad=2 Excellent=3 GOOD=4 VERY GOOD=5
print(s[["Quantitative Aptitude:","numberquantativeaptitude"]])
'''
lbmake=LabelEncoder()
df["numbercompany"]=lbmake.fit_transform(df["Company Name :"])+1
s=df[df["Company Name :"]=="unplaced"]
print(s[["numbercompany","Company Name :"]])#1 =placed 2=placed

print("Number of internship")
print(df[["numberinternship"]])
print("Number of events")
print(df["numberevents"])
print("Number of projects")
print(df["numberproject"])
df.to_csv("newc.csv", encoding='utf-8', index=False)