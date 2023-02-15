# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 09:04:41 2023

@author: DDas
"""
import pandas as pd
lst=['Geeks','For','Geeks','is','a','portal','for','geeks']
df1=pd.DataFrame(lst)
print(df1)
print(type(df1))
tp=('Geeks','For','Geeks','is','a','portal','for','geeks')
df2=pd.DataFrame(tp)
print(df2)
print(type(df2))
dictt1={"calories": [420, 380, 390],"duration": [50, 40, 45]}
df3=pd.DataFrame(dictt1)
print(df3)
print(type(df3))
dictt2={"Name":["Jai","Veeru","Raj","Aman"],
       "Age":[27,24,28,25],
       "Address":["Delhi","Kanpur","Allahabad","Patna"],
       "Qualification":["MSc","MA","MCA","Phd"]
      }
df4=pd.DataFrame(dictt2)
print(df4)
print(df4[["Name","Qualification"]])
row2=df4.iloc[2,1]
print(row2)
