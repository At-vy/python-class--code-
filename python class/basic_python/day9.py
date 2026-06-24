# Arrays in python 
# there ar three types of arrays in python
# 1. list (dynamic) / tuples
# 2. array module
# 3. numpy arrays
# array is a collection of items of same data type in contiguous manner
# this is array modeule
import array as array
# creating an array of integers
arr  = array.array('i', [1,2,3,4]) #'i' is type code for integer
print(arr)
# accessing elements of array
print(arr[0]) # 1
arr[1] = 10 # modifying element at index 1
print(arr) # array('i', [1, 10, 3, 4])
# traversing array
for i in arr:
    print(i)
# operations on array
# they have same operations as list
arr.append(5) # adding element to end of array
print(arr) # array('i', [1, 10, 3, 4, 5])
arr.insert(1,20)# inserting 20 at index 1
print(arr) # array('i', [1, 20, 10, 3, 4, 5])
# Numpy arrays
import numpy as np 
# creating numpy array
print("-----numpy array-----")
nparray = np.array([1,2,3,4,5])
print(nparray)
# 2d array
numarray2d = np.array([[1,2,3,],[4,5,6],[7,8,9]])
print(numarray2d)
# basic operations on numpy array
print("-----operations on numpy array-----")
# addition
# in 1d array
print("Addition:", nparray + 10)
# in 2d array
print("Addition in 2d array:\n", numarray2d + 10)
# using nested loops
for i in range(len(numarray2d)): #iterating through rows
    for j  in range(len(numarray2d[i])): #iterating through columns 
        numarray2d[i][j] = numarray2d[i][j] + 10