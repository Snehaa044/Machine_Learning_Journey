# #Python_Basics

f = "Python"
l = "Programming"

print("My first name is {} and last name is {}".format(f,l))


import numpy as np

arr = np.array([[1,2,3,4,5],[2,3,4,5,6],[9,7,6,8,9]])  # Creating an Array

print(arr[1:2,1:4]) # Slicing 

print(arr[arr<300]) #Return True if condition is true
print(arr%2)        #Returns elements after performing modulus operation

print(np.ones((2,5),dtype=int)) #Returns an array of ones
print(np.random.rand(5,3))      #Returns an array of random numbers of size 5X3
print(np.random.randn(5,3))     #Returns an array of random numbers of size 5X3 with mean 0 and std 1
print(np.random.randint(0,10,8).reshape(2,4))  #Returns an array of random integers of size 8 with values between 0 and 10 and reshaped
print(np.random.random_sample((5,3)))  #Returns an array of random decimal numbers of size 5X3


arr = np.array([1,2,3])

arr=np.array([[1,2,3,4,5],
      [2,3,4,5,6],
      [3,4,5,6,7]])
print(arr[0:2,3:])  #Returns an array after slicing





















# import numpy as np

# # Scalar
# a = 5

# # Vectors
# v = np.array([1, 2, 3])

# # Matrix
# marks = np.array([["Maths", "Science"], [40,50]])

# # Tensors
# n = np.random.rand(3, 3, 3)

# print("Scalar:", a)
# print("Vector:", v)
# print("Matrix:\n", marks)
# print("Tensor:\n", n)

# # Create a matrix representing marks of 5 students in 3 subjects.

# marks_of_5 = np.array(["Maths", "Science", "English"],[10,20,30],[20,30,40],[30,40,50],[12,34,45],[45,40,35])
# print("Marks of 5 students are:", marks_of_5)


