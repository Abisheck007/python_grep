import numpy as np
import random
a = np.array([1, 2, 3], dtype='int16')
b = np.array([4, 5, 6])
c  = a* b
# print("a:", a)

arr = np.array([[1, 2, 3, 4, 5, 6, 7], [8, 9, 10, 11, 12, 13, 14]])

#to get specific  data in arr

# print("I need 2 and 7 so I get", arr[0, 1], "and", arr[0, 6])

#to get specific row

# print(arr[1])

#to get specific column

# print(arr[:, 2])

#suppose if we need to take 2 4 6 out from array

# print(arr[0,1:6:2])

#let try to 3 6 9 12 from new array

arr1 = np.array([[1,2,3,4,5,6,7,8,9,10,11,12,13,14],[15,16,17,18,19,20,21,22,23,24,25,26,27,28]])

# print(arr1[0,2:13:3])

# print(arr1.size)

# to change value in numpy array

arr1[0,2] = 300

# print("After changing value in numpy array", arr1)

# print(np.ones((3, 4,2,4)))#this will create 3D array with 4 rows and 2 columns

# print(np.full((2,2),2))

# print(np.full_like(arr1,2))

#we can all pass random number inside our array

# print(np.random.randint(0, 10, size=(2, 3)))

#identity matrix

# print(np.identity(4, dtype='int16'))

# we can repear or array

# l1 = np.array([1, 2, 3])
# l2 = np.repeat(l1,3)
# print(l2)

#task1

# a = np.ones((7,7))
# a[1:6,1:6] = 0
# a[2:5,2:5] = 1
# a[3,3] = 9
# print(a)

#task2

# b = np.ones((9, 9))
# b[1:8, 1:8] = 0
# b[2:7, 2:7] = 1
# b[3:6, 4] = 0   
# b[4, 3:6] = 0 
# b[4, 4] = 9
# print(b)


#Linear algebra using  numpy
# a= np.full((2,3),1)
# b = np.full((3,2),2)
# print(np.matmul(a, b))

#statics using numpy

# stats = np.array([[1, 2, 3], [4, 5, 6]])
# print(np.max(stats, axis=1))
# print(np.sum(stats))

#rearranging array in numpy

# before = np.array([[1,2,3,4],[5,6,7,8]])
# after = before.reshape((2,2,2))  
# print(after)

#stacking vectors in numpy

# v1 = np.array([1, 2, 3])
# v2 = np.array([4, 5, 6])
# print(np.vstack((v1, v2, v1, v2)))  # vertical stacking if we use hstack then it will stack horizontally
# print(np.hstack((v1, v2, v1, v2)))  # horizontal stacking

#Load data from file

print(np.genfromtxt('/home/abisheck/python/python_grep/modules/data.txt', delimiter=','))