import numpy as np

a = np.array([1, 2, 3], dtype='int16')
b = np.array([4, 5, 6])
c  = a* b
print("a:", a)

arr = np.array([[1, 2, 3, 4, 5, 6, 7], [8, 9, 10, 11, 12, 13, 14]])

#to get specific  data in arr

print("I need 2 and 7 so I get", arr[0, 1], "and", arr[0, 6])

#to get specific row

print(arr[1])

#to get specific column

print(arr[:, 2])