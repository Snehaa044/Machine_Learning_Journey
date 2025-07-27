📌 NUMPY: Numerical Python

NumPy (Numerical Python) is a powerful library used for high-performance numerical and scientific computations in Python.

Why NumPy?
-----------
→ Faster computations than native Python lists  
→ Uses less memory (contiguous memory allocation)  
→ Supports multi-dimensional arrays  
→ Essential for Data Science, Machine Learning, and Scientific Computing

📥 INSTALLATION
----------------
pip install numpy

📦 IMPORTING
-------------
import numpy as np

🧊 ARRAY BASICS
-----------------
Array: A fixed-size container that holds elements of the same data type in contiguous memory locations.

✅ Advantages of NumPy Array over Python List:
- Array: Homogeneous, faster, less memory
- List: Heterogeneous, slower, more memory usage

🛠️ ARRAY CREATION METHODS
----------------------------
[1] From List
arr = np.array([1, 2, 3])

[2] 1D Array
arr1 = np.array([10, 20, 30])

[3] 2D Array using reshape()
arr2 = np.arange(1, 13).reshape(3, 4)
# Output: 3 rows × 4 columns filled with values from 1 to 12

📏 ARRAY ATTRIBUTES
---------------------
arr.shape      → Shape (rows, columns)  
arr.size       → Total number of elements  
arr.dtype      → Data type of elements  
arr.ndim       → Number of dimensions  
arr.itemsize   → Size of each item (in bytes)

🔁 ARRAY COPYING
-------------------
np.copy(arr) → Creates a deep copy; changes to the new array won’t affect the original array.

🚀 NUMPY FUNCTIONS – ONE-LINER CHEATSHEET
------------------------------------------
np.arange(start, stop, step)  
→ Returns evenly spaced values in a given interval  
e.g., np.arange(0, 10, 2) → [0 2 4 6 8]

np.linspace(start, stop, num)  
→ Returns 'num' evenly spaced values between start and stop (inclusive)  
e.g., np.linspace(0, 1, 5) → [0. 0.25 0.5 0.75 1.]

np.random.rand(d1, d2, ...)  
→ Returns random floats between 0 and 1 with shape (d1, d2, ...)

np.random.randn(d1, d2, ...)  
→ Returns samples from standard normal distribution (mean=0, std=1)

np.random.random_sample(shape)  
→ Returns random floats in [0.0, 1.0) — same as rand

np.random.randint(low, high, size)  
→ Random integers between [low, high)

📌 CONDITIONS & OPERATIONS IN NUMPY
-------------------------------------
✅ Conditions:
→ NumPy allows applying conditions directly:
Example:
  arr = np.array([10, 100, 200])
  arr < 100 → [True, False, False]

✅ Arithmetic Operations:
→ Supports element-wise operations:
  - arr + 2
  - arr1 * arr2
  - arr // 2
→ No need for loops — operations are vectorized

🎯 SUMMARY
-------------
✔ NumPy = Speed + Simplicity for numerical work  
✔ Used in ML, Data Analysis, Deep Learning, and more  
✔ Mastering NumPy is foundational for any Data/ML/AI journey
