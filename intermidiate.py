#Indexing in Numpy Array

import numpy as np
# arr = np.array([10,20,30,40,50,60])
# print(arr)
# print(arr[0])
# print(arr[1])
# print(arr[2])
# print(arr[-1])


#Slicing in Numpy Array

# arr = np.array([10,20,30,40,50,60])
# print(arr[1:4])
# print(arr[:3])
# print(arr[::-1])
# print(arr[::2])  #arr[start:stop:step]


#Filtering Data or Called Boolean Masking

# arr = np.array([10,20,30,40,50,60])
# print(arr[arr>25]) # Condition inside this Function
# print(arr[arr%3==0])



#Reshaping and Manupulating the Data

# arr = np.array([10,20,30,40,50,60])
# print(arr.reshape(2,3))
# print(arr.reshape(3,2))


#rival()-->For View Effect the Original Data
#flatten()-->Copy Do not Effect Tthe Original Data

arr_2d = np.array([[1,2,3],
                   [4,5,6]])
print(arr_2d.ravel())
print(arr_2d.flatten())
