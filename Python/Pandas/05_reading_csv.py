import pandas as pd
import numpy as np
from io import StringIO, BytesIO    # Importing StringIO and BytesIO classes from the io module

# 🔹 Load data from CSV file into a DataFrame
data = pd.read_csv("test.csv")   #Defualt sep = ','
data2 =pd.read_csv("test2.csv",sep=";")

# 🔹 Print the entire dataset (⚠️ avoid for very large datasets)
print(data)
print(data2)

#Returns Datatype of test.csv as 'str'
print("Datatype of test.csv is",type("test.csv"))   

data3= """,c1,c2,c3\n
        r1,1,2,3\n
        r2,4,5,6\n
        r3,7,8,9\n"""

print("Converting string 'data3' to dataframe")
df3=pd.read_csv(StringIO(data3), dtype=object)   # 'object' datatype simply means string
print(df3)
print("Datatype of df3 is",type(df3))

print("Reading from specific columns:\n")
print(pd.read_csv(StringIO(data3),usecols=["c1","c3"]))

#Converting Dataframe 'df3' to csv file
print(df3.to_csv("test3.csv"))

#Accessing a particular element
print(df3['c1'][1])

data4= 'c1,c2,c3\n''10,20,30\n''40,50,60\n''70,80,90'
print(data4)

print("Converting string 'data4' to dataframe")
df4=pd.read_csv(StringIO(data4),dtype=int) 
print(df4) 

print("Datatype of df4 is",type(df4))

#Display the column elements of df4
print(df4['c1'])
print(df4['c1'][2])

#Changing datatype into float
df5=pd.read_csv(StringIO(data4),dtype=float) 
print(df5) 

print("Datatype of df4 is",type(df5))

#Display the column elements of df5
print(df5['c1'])
print(df5['c1'][2])


#Changing datatype of different columns into float, int, Int64
df6=pd.read_csv(StringIO(data4),dtype={'c1':float, 'c2':int, 'c3':'Int64'}) 
print("df6 is\n",df6) 

print("Datatype of df6 is",type(df6))

#Display the column elements of df6 and its datatype
print(df6['c1'])
print(type(df6['c1']))

print(df6['c2'])
print(type(df6['c2']))

print(df6['c3'])
print(type(df6['c3']))

#Access a particular column element and its datatype
print(df6['c1'][2])
print(type(df6['c1'][2]))

#Check datatypes
print("Datatypes of df6:\n")
print(df6.dtypes)

#To use a particular column as the index of the resulting DataFrame.
df7=pd.read_csv(StringIO(data4),index_col=0)
print("df7 is:\n",df7)

df8=pd.read_csv(StringIO(data4),index_col=1)
print("df8 is:\n",df8)

#
data5=('c1,c2,c3\n' 
       '10,apple,bat,\n'
       '20,orange,ball,')
print("data5:\n",data5)

#If the first value is a number, it considers as index
df9=pd.read_csv(StringIO(data5))
print("df9 is:\n",df9)

# If index_col= False, then it won't consider first value as index
df10=pd.read_csv(StringIO(data5),index_col=False)
print("df10 is:\n",df10)

#Quoting and Escape characters useful in NLP

data='a,b\n"Hello,\\"Bob\\",nice to meet you",5'
df11=pd.read_csv(StringIO(data))
print("With escape character:\n",df11)

df12=pd.read_csv(StringIO(data),escapechar='\\')
print("Without escape character:\n",df12)

# URL to csv

df13=pd.read_csv('https://download.bls.gov/pub/time.series/cu/cu.item',sep='\t')
print("URL to csv:\n",df13.head())