import numpy as np

#2D array representation
arr = np.array([[1,1,45,3,4,5,7],[44,32,21,2,3,4,9]])
print(arr[0,0:5])
print(arr[0:2, 2])
print(arr[0:2, 1:4])

#3D array representation
arr = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print(arr[1,0,1])


arr = np.array([[1,2,3,4,5]])
print(arr.dtype)
arr = np.array([1.1, 2.1, 3.1])

print(arr.dtype)

#Type casting
newarr = arr.astype('i')

print(newarr)
print(newarr.dtype)