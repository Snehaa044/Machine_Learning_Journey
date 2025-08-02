import pandas as pd

# Sample data
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 22],
    'City': ['New York', 'Los Angeles', 'Chicago']
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Save it as an Excel file
df1=df.to_excel('Excel.xlsx', index=False)  # index=False avoids writing row numbers

print("Excel file created successfully!")

print("df1Excel data is:\n",df1)


#  Reading a csv file
#  -----------------
df2= pd.read_excel('Excel_sample.xlsx')
print("df2 Excel Data is:\n", df2)

# To print only the first five rows
print("df2 Excel Data is:\n", df2.head())

# Pickling or Serialization

#Coverting dataframe df into pickle file - df4
df3=df.to_pickle('df4')
print(pd.read_pickle('df4'))