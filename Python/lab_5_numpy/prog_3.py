#USE OF COPY AND VIEW

import numpy as np

arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()
arr[0] = 42

print(arr)

print(x)

arr = np.array([1, 2, 3, 4, 5])
x = arr.view()
arr[0] = 42

print(arr)

print(x)


print("#Checking the Shape of an array")
arr = np.array([[1,2,3,4],[5,6,7,8],[7,8,9,0],[3,2,4,5]])
print(arr)
print(arr.shape)

print("#Reshaping the Array")

print("#1D to 2D")
arr = np.array([1,2,3,44,5,6,7,8,9])
new_array = arr.reshape(3,3)
print(new_array)

print("#1D to 3D")
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = arr.reshape(2, 3, 2)
print(newarr)

print("#Undimentional Array Reshaping")
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = arr.reshape(2,-1)
print(newarr)

print("#CONVER AN 2D ARRAY TO 1D ARRAY")
arr = np.array([[1,2,3,4],[5,6,7,8],[7,8,9,0],[3,2,4,5]])
new_array = arr.reshape(-1)
print(new_array)

print("#COVERT AN 3D ARRAY TO 1D ARRAY")
arr = np.array([[[1,2,3,4],[5,6,7,8]],[[7,8,9,0],[3,4,5,6]]])
new_array = arr.reshape(-1)
print(new_array)



print("#ITERATING THE ARRAYS")
arr = np.array([[1,2,3,4],[2,3,4,5]])
for x in arr:
    print(x)
    
print("#ITERATING USING TWO LOOPS")
arr = np.array([[1,2,3,4,5],5,6,7,8,9])
for x in arr:
    for y in x:
        print(y)