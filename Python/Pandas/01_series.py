import pandas as pd
import numpy as np

#Series - One row & One Column

#Creation of Series
#[1] From list

series = pd.Series([1, 2, 3, 4, 5])
print("Series from list:\n",series)

data = [10,20,30,40]
series1 =pd.Series(data)
print(series1)

#Custom Index

series2 =pd.Series([11,22,33,44,55], index=['a','b','c','d','e'])
print(series2)

#From Dict
series3=pd.Series({"Math":68,"Science":55})
print("Series from dict:\n",series3)

#Series created using Numpy
series4 = pd.Series(np.array([100, 200, 300, 400,500]))
print(series4)