import numpy as np


# Ceartion of 1D Array

# arr = np.array([1,2,3,4])
# print(arr)

#Creation of 2D Array

# arr = np.array([[1,2,3],
#                 [4,5,6]])
# print(arr)

#Creation of Multi-D Array

# arr = np.array([[1,2,3],
#                 [4,5,6],
#                 [7,8,9]])
# print(arr)


#Array Filled with Zeros

# arr = np.zeros((3,2))
# print(arr)


# Array Filled with Once

# arr = np.ones((2,2))
# print(arr)

#Filed with default Values

# arr = np.full((3,2),6)
# print(arr)

#Creating a Sequence of Number
# arr = np.arange(1,20,3)
# print(arr)

#Creating Identity Matrix

# arr = np.eye(3)
# print(arr)

# arr = np.array([[1,2,3],
#                 [4,5,6]])
# print(arr.shape)
# print(arr.size)
# print(arr.ndim)
# print(arr.dtype)


# arr = np.array(["Raj","Baishaki","Shiva"])
# print(arr.dtype)

#Converting one Data Type to Annother Data Type

# arr = np.array([2.4,4.5,5.5])
# int_arr = arr.astype(int)
# print(int_arr.dtype)

#Aggragiate Function on Numpy Array
# arr = np.array([10,20,30,40,50])
# print(np.sum(arr))
# print(np.mean(arr))
# print(np.max(arr))
# print(np.min(arr))
# print(np.std(arr))


#Differnt Operation on Numpy Array

# arr = np.array([10,20,30,40,50])
# print(arr+5)
# print(arr*2)
# print(arr**2)
# print(arr%2)
# print(arr/2)
# print(arr//2)