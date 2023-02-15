#FITERING IN NUMPY

#Create a filter array that will return only values higher than 42:
import numpy as np
arr = np.array([41, 42, 43, 44])

filtered_array = []

for i in arr:
    if i > 42:
        filtered_array.append(True)
    else:
        filtered_array.append(False)

new_array = arr[filtered_array]
print(arr)
print(filtered_array)
print(new_array)