import pandas as pd
import numpy as np

#DataFrame means more than one column and more than one row

#Creating a DataFrame with 10 rows and 4 columns with random integers between 0-100
df = pd.DataFrame(np.random.randint(0, 100, size=(10, 4)), columns=["Col1", "Col2", "Col3", "Col4"])
print(df)           # Prints the whole DataFrame
print(df.head())    # Prints the first 5 rows

#Creation of DataFrame
data=pd.DataFrame([1,2,3])
print(data)

data1=pd.DataFrame([[1,2,3],[2,3,4]])
print(data1)
print(data1.head(1)) #Returns only first row
print(data1.head(2)) #Returns first two rows
print(data1.head())  #Returns all rows


#Creation of DataFrame using numpy

#df=pd.DataFrame(data,rows, columns, dtype)
data=pd.DataFrame(np.array([[1,2,3],[2,3,4]]))
print(data)

data2=pd.DataFrame(np.arange(0,16,2).reshape(2,4),index=["Row1","Row2"], columns=["Col1","Col2", "Col3", "Col4"]) 
print(data2)

#Creation of csv file from DataFrame
data2.to_csv("test.csv")        #Creates a csv file
print(data2.to_csv("test.csv")) #Returns None and csv file is created with data