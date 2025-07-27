import numpy as np

arr = np.array([1,2,3,4,5,6])
print(arr)

arr2 = np.array([[1,2,3],
                 [4,5,6],
                 [7,8,9]])
print(arr2)

#Creation of 1D Array with evenly spaced values (like range) with start, stop, step size
print(np.arange(0,10)) 
print(np.arange(0,10,2)) 
print(np.arange(1,18,3)) 

#Returns an array of ones in the range given
print(np.ones((2,5),dtype=int)) 

#Returns an array of random numbers of size 5X3
print(np.random.rand(5,3))    

#Returns an array of random decimal numbers of size 5X3
print(np.random.random_sample((5,3)))  

#Returns an array of random numbers of size 5X3 with mean 0 and standard deviation 1
print(np.random.randn(5,3))    

#Returns an array of random integers of size 8 with values between 0 and 10 and reshaped
print(np.random.randint(0,10,8)) 
print(np.random.randint(0,10,8).reshape(2,4))
print(np.random.randint(0,10,8).reshape(4,2))

#Creates 'num' evenly spaced values between start and stop (inclusive) with stepvalue.
print(np.linspace(0,1,5))
print(np.linspace(0,10,20))

#Copy function
arr3 = arr.copy()
print("arr3 is",arr3)
print("arr is",arr)

#Making a change in arr3 - It won't affect arr
arr3[3:]=500
print("arr3 after change is",arr3)
print("arr after modification of arr3 is",arr)

#Creates an array of ones
print(np.ones(4,dtype=int))
print(np.ones(4))                #By default, dtype=int
print(np.ones((2,5),dtype=int))  #2D Array of size 2 X 5