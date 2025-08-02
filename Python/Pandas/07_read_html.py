import pandas as pd
import numpy as np

url='https://www.fdic.gov/bank/individual/failed/banklist.html'
df=pd.read_html(url)
df1=pd.read_html(url,match="City",header=None)
print("HTML Content of df is:\n",df)
print("HTML Content of df1 is:\n",df1)

#To find total tables
print("Total tables found:", len(df))

#Returns Datatype of df
print("Datatype of df is:\n",type(df))
