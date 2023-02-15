import numpy as np
a = np.array([1,2,3])
print(np.__version__)
a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(a," ",a.ndim,"'D Array")
print(b," ",b.ndim,"'D Array")
print(c," ",c.ndim,"'D Array")
print(d," ",d.ndim,"'D Array")