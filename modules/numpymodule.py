import numpy as np

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

print(np.full_like(arr1,2))