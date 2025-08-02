import pandas as pd
import numpy as np

# ---------------------------------------------
# ✅ Reading JSON string and converting to DataFrame
# The JSON is a list of dictionaries, each representing a row
data = '[{"employee":"James","age":30}]'
df = pd.read_json(data)
print("DataFrame from JSON string is:\n", df)

# ---------------------------------------------
# ✅ Reading CSV from a URL
# UCI Wine dataset is loaded with no header (raw data)
df1 = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data', header=None)
print("\nFirst 5 rows of wine dataset:\n", df1.head())

# ---------------------------------------------
# ✅ Saving DataFrame `df1` to a CSV file named 'wine.csv'
df1.to_csv('wine.csv', index=False)
print("\n✅ Created a file named 'wine.csv' with the wine dataset")

# ---------------------------------------------
# ❌ Wrong way: Just printing the function object (not the actual JSON)
print("\n❌ This just prints the function reference, not the actual JSON:")
print(df.to_json)     # prints something like <bound method DataFrame.to_json of ...>
print(df1.to_json)

# ---------------------------------------------
# ✅ Correct way: Call the method with parentheses to get JSON string
print("\n✅ Correctly converted DataFrame to JSON string:")
print(df.to_json())   # converts df to JSON string format
print(df1.to_json())  # converts df1 to JSON string format

# Convert Json to different Json formats
print(df.to_json(orient= "records")) # Convert the DataFrame rows into a list of dictionaries, where each row becomes one dictionary (i.e., one "record").

