import numpy as np

#Converting List into Array
list = [1,2,3,4,5]
arr =np.array(list)
print(arr)

print(type(arr))

#One-dimensional Array Creation
arr = np.array([1,2,3,4,5,6])

#Find Shape or Size of Array
print(arr.shape)

#Convert !D Array into 2D Array
print(arr.reshape(2,3))

#2D Array creation

arr2 = np.array([[1,2,3],
                 [4,5,6],
                 [7,8,9]])
print(arr2)
print(type(arr2))
print(arr2.shape)

#2D Array creation using multiple lists

list1 = [1,2,3,4]
list2 = [5,6,7,8]

arr3 = np.array([list1,list2])
print(arr3)
print(arr3.shape)
print(arr3.size)

#Converting the size of arr3 from 4 X 2 to 2 X 4
print(arr3.reshape(4,2))

