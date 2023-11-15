# Ex-01_DS_Data_Cleansing :

## DATE :24/08/2023

## AIM :
To read the given data and perform data cleaning and save the cleaned data to a file. 

# Explanation
Data cleaning is the process of preparing data for analysis by removing or modifying data that is incorrect ,incompleted , irrelevant , duplicated or improperly formatted. 
Data cleaning is not simply about erasing data ,but rather finding a way to maximize datasets accuracy without necessarily deleting the information. 

# ALGORITHM :
### STEP 1
Read the given Data
### STEP 2
Get the information about the data
### STEP 3
Remove the null values from the data
### STEP 4
Save the Clean data to the file

# CODE :
```
Developed By : Shree Ram R
reference number: 212222040154
```
```python

import pandas as pd
import numpy as np

df=pd.read_csv("data.csv")
df

df.head()

df.shape

df.tail()

df.describe()

df.isnull().sum()

df.dropna(how="any").shape

df.dropna(how="any")

df.dropna(how="all").shape

df.dropna(how="all")

tot=df.dropna(subset=['M4'],how="any")
tot

tot=df.dropna(subset=['M1','M2','M3','M4'],how="any")
tot

df.fillna(0)

df.fillna(method='ffill')



df.fillna(method='bfill')

mn=df.TOTAL.mean()
mn

df.TOTAL.fillna(mn,inplace=True)
df

l=df.M1.interpolate()
l

me=df.M2.median()
me

mo=df.M3.mode()
mo

df.duplicated()

df.drop_duplicates(inplace=True)
df

df['cd']=pd.to_datetime(df['DOB'])
df

for i in df.index:
    if df.loc[i,"AVG"]>100:
              df.drop(i,inplace=True)
df
```


#Output:
![image](https://github.com/gururamu08/ODD2023-Datascience-Ex01/assets/118707009/e45c5ac4-0e47-4164-b0b6-d30e30704a31)

![image](https://github.com/gururamu08/ODD2023-Datascience-Ex01/assets/118707009/bbb63c56-b62d-46fc-b33c-4496f755b433)

![263434174-fc5646bc-5f09-4449-a810-d1a96af0e759](https://github.com/gururamu08/ODD2023-Datascience-Ex01/assets/118707009/082544b5-da90-4796-8e07-9382a2813217)

![263434193-ca663b59-7790-4de7-8813-0ba1e9a2f20d](https://github.com/gururamu08/ODD2023-Datascience-Ex01/assets/118707009/47ab0428-9581-4cf0-9374-2bfafd1bcce1)

![263434212-459aae91-2394-4437-bd3e-fd769c0b19c1](https://github.com/gururamu08/ODD2023-Datascience-Ex01/assets/118707009/fa196ea9-8c8a-4408-9ff7-bc7473ecd74d)


![264390625-7a74c202-8c08-4e34-bf58-0d74a6592a1f](https://github.com/gururamu08/ODD2023-Datascience-Ex01/assets/118707009/7f88c711-9311-4899-9793-0f14b1899c9a)


![264390924-04f9e304-b435-4e93-85ba-4c07407b3424](https://github.com/gururamu08/ODD2023-Datascience-Ex01/assets/118707009/e2ff1319-77a9-4292-be6f-827149b275a1)

![264391104-50d5dd78-1448-44f9-91dc-e73daaaf32ba](https://github.com/gururamu08/ODD2023-Datascience-Ex01/assets/118707009/36d645a8-561b-4e3a-ba7b-d480cd15fb9c)

![264391251-f84ee951-285d-4c8b-acc9-0f3a3f575fc5](https://github.com/gururamu08/ODD2023-Datascience-Ex01/assets/118707009/3882b218-a3b5-4c2b-9fb1-f304d1755bff)

![264391391-d0a40e81-1a2a-4d3e-bf07-9c9e5ef53609](https://github.com/gururamu08/ODD2023-Datascience-Ex01/assets/118707009/a09fa29b-a8eb-4642-b220-5b23e8424499)

![264391546-96705cb6-fbb7-49bc-9760-8d21a9f68afc](https://github.com/gururamu08/ODD2023-Datascience-Ex01/assets/118707009/63b0d88f-be64-43be-8684-cf5fa97d42cb)
![264391800-95c12089-8421-4ed5-8f0a-406df11fe301](https://github.com/gururamu08/ODD2023-Datascience-Ex01/assets/118707009/ab368a01-501b-4ace-8e69-4b914b630cf6)



![264391800-95c12089-8421-4ed5-8f0a-406df11fe301](https://github.com/gururamu08/ODD2023-Datascience-Ex01/assets/118707009/02e21a28-1d67-4bda-bfe7-5e95d23ce8d1)
![264391914-51a38697-0154-47c6-8a19-deae3f27fc03](https://github.com/gururamu08/ODD2023-Datascience-Ex01/assets/118707009/b5c8534e-25b3-4a1d-a026-6029ff328a7c)

![264392035-4227fcf7-13fc-449c-81dc-f7f636b9f24d](https://github.com/gururamu08/ODD2023-Datascience-Ex01/assets/118707009/de7a5a78-9f01-4035-b218-cf74cdf7e3e7)

![264392142-89333abe-f635-4dbb-8883-33facbfce7fa](https://github.com/gururamu08/ODD2023-Datascience-Ex01/assets/118707009/0da375d6-564b-49e5-9b9d-fddfe8b76184)



![264392346-4fe12bc3-8493-4219-b10d-5c2bdc9227fb](https://github.com/gururamu08/ODD2023-Datascience-Ex01/assets/118707009/84849b50-acc5-470b-85d6-9b907e11e051)


![264392515-c8d2bf8b-6a27-4dfd-bb96-60c6dbfce3c6](https://github.com/gururamu08/ODD2023-Datascience-Ex01/assets/118707009/abcb5b57-dc06-4bad-908d-90a06b9ac31d)


![264392809-c18987d5-1c58-4c04-a13d-dfc1aa474d1d](https://github.com/gururamu08/ODD2023-Datascience-Ex01/assets/118707009/abf339ed-afe2-437d-99bd-0818597fadb1)
![264392962-6d413529-a351-492b-9812-ea04110bb6f2](https://github.com/gururamu08/ODD2023-Datascience-Ex01/assets/118707009/2a91e39b-9477-4b2d-b20a-ae9242799478)


![264393106-3ac63188-fe54-4bd0-944a-48f460cf5bdb](https://github.com/gururamu08/ODD2023-Datascience-Ex01/assets/118707009/4b2c230c-b46d-4756-bf5f-0e9453ba5600)

![264393225-b08e8841-7e81-4fd6-b47e-ea1b5da72310](https://github.com/gururamu08/ODD2023-Datascience-Ex01/assets/118707009/f6ad9aca-7f46-40c6-abe0-972e6165664b)
![264393340-725b9178-0e45-4dde-9a15-86849618a668](https://github.com/gururamu08/ODD2023-Datascience-Ex01/assets/118707009/dd54e103-5824-47d9-9e33-a909cf9d4024)

![264393481-1512188d-b0e6-4eea-be7f-5827e8e270dc](https://github.com/gururamu08/ODD2023-Datascience-Ex01/assets/118707009/84906ae0-c61b-4134-816d-66ec0624695c)


## RESULT:
Thus the given data is read,cleansed and the cleaned data is saved into the file.
