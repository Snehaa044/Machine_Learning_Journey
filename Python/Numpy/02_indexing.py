import numpy as np

arr= np.array([[1,2,3,4,5],
               [2,3,4,5,6],
               [9,7,6,8,9]])  # Creating an Array

#Accessing a row
print(arr[1])

#Accessing an element in a row
print(arr[1][2])

#Slicing few rows and columns

print(arr[1:,2:]) # Accessing all rows except the first and all columns except the first two
print(arr[:,:])   # Accessing all rows and columns
print(arr[:,1:])  # Accessing all rows and all columns except the first one
print(arr[0:2,3:]) #Returns an array after slicing


