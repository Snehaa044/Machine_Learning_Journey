
# 📊 Pandas

This repository covers **essential Pandas operations** from **Series creation** to **DataFrames, CSV, JSON, HTML, Excel handling**, and **Pickling ML data**.

---
Pandas : Open-source and high performance Python library used as a tool for data analysis

Import pandas  : 



## 📥 Installation

pip install pandas numpy

## 📥 Importing Pandas

import pandas as pd

## 🧵 Series — One-dimensional data
Series : One row and One Column

DataFrame : Multiple rows and Columns

### 📌 Creating Series
```python
# From list
series = pd.Series([1, 2, 3, 4, 5])

# Custom Index
series2 = pd.Series([11,22,33], index=['a','b','c'])

# From Dictionary
series3 = pd.Series({"Math": 68, "Science": 55})

# Using NumPy Array
series4 = pd.Series(np.array([100, 200, 300]))
```

---

## 💃 DataFrame — Two-dimensional data
### 📌 Creating DataFrames
```python
# From NumPy Arrays
df = pd.DataFrame(np.random.randint(0, 100, size=(10, 4)), columns=["Col1", "Col2", "Col3", "Col4"])

# From List of Lists
data1 = pd.DataFrame([[1,2,3],[2,3,4]])

# Using np.arange() with reshape()
data2 = pd.DataFrame(np.arange(0,16,2).reshape(2,4), index=["Row1","Row2"], columns=["Col1","Col2","Col3","Col4"])
```

---

## 📊 DataFrame Operations
### 📌 Accessing Elements
```python
df.loc["Row1"]     # By index name
df.iloc[0:4, 2:4]  # By index position
df.iloc[:, 1:]     # Slicing columns
```

### 📌 Converting DataFrame to Numpy Array
```python
df.iloc[:, 1:].values
```

### 📌 Value Counts & Unique Values
```python
df["Col1"].value_counts()   # Count unique values
df["Col1"].unique()         # Show unique values
```

---

## 🔍 Checking Null Values
```python
df.isnull()          # Boolean DataFrame for nulls
df.isnull().sum()    # Count of nulls per column
```

---

## 📂 CSV File Operations
### 📌 Reading & Writing CSV
```python
# Read CSV
df = pd.read_csv("test.csv")

# Write to CSV
df.to_csv("output.csv", index=False)
```

### 📌 Reading from URL (CSV)
```python
df = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data', header=None)
```

---

## 📝 Reading CSV from String Data
```python
from io import StringIO

data = 'c1,c2,c3\n10,20,30\n40,50,60'
df = pd.read_csv(StringIO(data))
```

### 📌 Changing Data Types while Reading CSV
```python
df = pd.read_csv(StringIO(data), dtype={'c1': float, 'c2': int, 'c3': 'Int64'})
```

### 📌 Using Specific Column as Index
```python
df = pd.read_csv(StringIO(data), index_col=0)
```

---

## 🛉 Quoting & Escape Characters in CSV (Useful in NLP)
```python
data='a,b\n"Hello,\\"Bob\\",nice to meet you",5'
df = pd.read_csv(StringIO(data), escapechar='\\')
```

---

## 🌐 Reading Tables from HTML
```python
url = 'https://www.fdic.gov/bank/individual/failed/banklist.html'
df = pd.read_html(url)  # List of tables
df1 = pd.read_html(url, match="City", header=None)  # Match a table containing 'City'

print("Total tables found:", len(df))
```

---

## 📅 Excel File Operations
```python
# Write to Excel
df.to_excel('Excel.xlsx', index=False)

# Read from Excel
df2 = pd.read_excel('Excel_sample.xlsx')
```

---

## 🔢 JSON File Operations
```python
# Read JSON
json_data = '[{"employee":"James","age":30}]'
df = pd.read_json(json_data)

# Convert DataFrame to JSON String
df.to_json()                  # Default orientation
df.to_json(orient="records") # Record-wise JSON format
```

---

## 📥 Pickling (Serialization of DataFrames)
```python
# Save DataFrame to Pickle file
df.to_pickle('df_pickle')

# Load Pickle file
pd.read_pickle('df_pickle')
```

---

## 📚 Summary
This repo covers:
- Series & DataFrame creation
- Indexing, Slicing
- CSV, JSON, Excel, HTML reading & writing
- Data Type conversion
- Null checks, Value counts
- Quoting/Escape characters in CSV (NLP)
- Pickling DataFrames for ML models

---

> 📢 **This is a Pandas   Ready-Reckoner for Machine Learning Data Handling.**

---

📑 **Author:** Sneha S S
📚 **References:** [Pandas Documentation](https://pandas.pydata.org/docs/)
