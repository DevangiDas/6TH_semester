import numpy as np
#JOINING TWO ARRAYS IN NUMPY

arr1 = np.array([1,2,3,4])
arr2 = np.array([5,6,7,8])

arr = np.concatenate((arr1,arr2))
print(arr)

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.concatenate((arr1, arr2))
print(arr)
arr = np.stack((arr1, arr2), axis=1)
print(arr)

#SEARCHING IN NUMPY

#Finding the indexes where the searched element is present
arr = np.array([1, 2, 3, 4, 5, 4, 4])
x = np.where(arr == 4)
print(x)

#Finding the elements those are even in an array
arr = np.array([[3,4,5],[2,1,6]])
x = np.where(arr%2 == 0)
print(x)


#SORTING ARRAYS IN NUMPY
arr = np.array([12,19,2,5,50,8,5,16])
print(np.sort(arr))