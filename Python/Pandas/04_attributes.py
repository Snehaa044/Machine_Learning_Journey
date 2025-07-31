import pandas as pd
import numpy as np

# df=pd.DataFrame(np.arange(0,20).reshape(5,4),index=["Row1","Row2","Row3","Row4","Row5"], columns=["Col1","Col2","Col3","Col4"],dtype=None)
# print(df.head())

#Check if null values exists

data = {
    "Name": ["Alice", "Bob", "Charlie", None,None],
    "Age": [25, None, 30, 22,55]
}

df = pd.DataFrame(data)
print(df)
print(df.isnull())          #If null,returns True
print(df.isnull().sum())    #Returns the count of null values in each column

#Readung a csv file
data = pd.read_csv("test.csv") 
print(data)

# 🔹 Gives info about the DataFrame: 
#    - Number of non-null entries
#    - Data types of each column
#    - Memory usage
print("Information about data is:\n",data.info())


# 🔹 Gives statistical summary of numeric columns:
#    - count, mean, std, min, max, quartiles (25%, 50%, 75%)
print(data.describe())

