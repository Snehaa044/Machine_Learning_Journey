import pandas as pd
import numpy as np

df=pd.DataFrame(np.arange(0,20).reshape(5,4),index=["Row1","Row2","Row3","Row4","Row5"], columns=["Col1","Col2","Col3","Col4"],dtype=None)
print(df.head())

#Accessing elements
#Two methods 1) .loc - Row indexes only 2) .iloc - Row and Column index

print(df.loc["Row1"])           #Returns Row1 values
print(type(df.loc["Row1"]))     #Returns Datatype

print(df.iloc[0:4,2:4])         
print(type(df.iloc[0:4,2:4]))
      
print(df.iloc[:,1:])
print(type(df.iloc[:,1:]))

#Converting DataFrames into Array

print(df.iloc[:,1:].values)       #Returns rows and columns without having headings as index
print(df["Col1"].value_counts())  #Returns counts of unique values in a column

data=pd.DataFrame([[1,20,3],[10,20,3],[1,20,3]],index=["Row1","Row2","Row3"], columns=["Col1","Col2","Col3"])
print(data["Col1"].value_counts())  #Returns count of unique values in Col1
print(data["Col2"].value_counts())  #Returns count of unique values in Col2

#Returns only unique values in a particular column
print("Unique values in Col1 is:\n",data["Col1"].unique)

#Accessing a particular column elements
print(data['Col1'])