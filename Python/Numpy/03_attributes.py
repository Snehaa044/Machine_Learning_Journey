import numpy as np

arr = np.array([1,2,3,4,5,6])
print(arr)

arr2 = np.array([[1,2,3],
                 [4,5,6],
                 [7,8,9]])
print(arr2)

#Return Datatype of Elements
print("Datatype of arr=",arr.dtype)
print("Datatype of arr2=",arr2.dtype)

#Returns number of dimensions
print("Number of dimensions arr=",arr.ndim)
print("Number of dimensions arr2=",arr2.ndim)


#Creating an array of datatype int32
arr3 = np.array([10, 20, 30], dtype=np.int32)

#Returns the size (in bytes) of one element in the array.
print("Size (in bytes) of one element in arr",arr.itemsize)
print("Size (in bytes) of one element in arr2",arr.itemsize)
print("Size (in bytes) of one element in arr3",arr3.itemsize)

#Returns total number of elements
print("Total number of elements in arr,arr2, arr3 are : \n")
print(arr.size)
print(arr2.size)
print(arr3.size)


#Returns total memory used (size × itemsize)
print("Total memory used in arr,arr2, arr3 are : \n")
print(arr.nbytes)  
print(arr2.nbytes)
print(arr3.nbytes)
