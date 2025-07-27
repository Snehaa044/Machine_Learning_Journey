import pandas as pd
import numpy as np

#df=pd.DataFrame(data,rows, columns, dtype)
df=pd.DataFrame(np.arange(0,20).reshape(5,4),index=["Row1","Row2","Row3","Row4","Row5"], columns=["Col1","Col2","Col3","Col4"],dtype=None)
print(df.head())
# print(df.to_csv("Test.csv"))


#DataFrame means more than one column andmore than one row
#DataSeries one column and one row

#Accessing elements
#Two methods 1) .loc - Row indexes only 2) .iloc - Row and Column index

# print(df.loc["Row1"])
# print(type(df.loc["Row1"]))

# print(df.iloc[0:4,2:4])
# print(df.iloc[:,1:])

# Converting DataFrames into Array

# print(df.iloc[:,1:].values)
print(df["Col1"].value_counts())

# Check if null values exists

# data = {
#     "Name": ["Alice", "Bob", "Charlie", None],
#     "Age": [25, None, 30, 22]
# }

# df = pd.DataFrame(data)
# print(df.isnull())
# print(df.isnull().sum())


