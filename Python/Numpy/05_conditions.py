import numpy as np

arr = np.array([1,2,3,4,5,6])
print(arr)

arr2 = np.array([[1,2,3],
                 [4,5,6],
                 [7,8,9]])
print(arr2)


#Conditions (Useful in EDA - Exploratory Data Analysis)

var = 100
print(var < arr)   # Element-wise comparison → [True, True, ..., True]

var2 = 3
print(var2 < arr)  # Compares 3 with each element in arr

#Array Operations

print(arr2 * 2)     # Element-wise multiplication by 2
print(arr // 2)     # Integer division of each element in arr by 2

print(arr[arr<300]) #Returns True if condition is true
print(arr%2)        #Returns elements after performing modulus operation


