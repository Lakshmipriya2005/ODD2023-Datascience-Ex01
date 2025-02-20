# -*- coding: utf-8 -*-
"""assign 1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1fQ5QnaAfrNJ0p6sDjtSmqOz2XiEBD6L5
"""

import pandas as pd
import numpy as np

df=pd.read_csv("data.csv")
df

df.head()

df.shape

df.tail()

df.describe()

df.isnull().sum()#used to sum the total null valuse in data set

df.dropna(how="any").shape

df.dropna(how="any")#delete the row if any of the column is empty

df.dropna(how="all").shape#to find number of rows and columns

df.dropna(how="all")#delete the row if all column is null.

tot=df.dropna(subset=['M4'],how="any")
tot

tot=df.dropna(subset=['M1','M2','M3','M4'],how="any")#delete the row which any one of the subset is null.
tot

df.fillna(0)#fill the null valuse with zero.

df.fillna(method='ffill')#fill with pervious row values where the values are null.



df.fillna(method='bfill')#fill with next row values where the values are null.

mn=df.TOTAL.mean()#to find the mean vvalue ofor particular column.
mn

df.TOTAL.fillna(mn,inplace=True)#replace the null value of the particular column with mean value
df

l=df.M1.interpolate()#it is the anothe method like "mean" to fill null values.
l

me=df.M2.median()#it is used to find the  middle value when is order in ascending order.
me

mo=df.M3.mode()# it is used to find the value whis is repeated frequently.
mo

df.duplicated()#check the duplicate values

df.drop_duplicates(inplace=True)
df

df['cd']=pd.to_datetime(df['DOB'])
df

for i in df.index:
    if df.loc[i,"AVG"]>100:
              df.drop(i,inplace=True)
df