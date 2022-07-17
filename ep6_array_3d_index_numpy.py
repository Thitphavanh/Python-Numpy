# Array 3D index
import numpy as np

# array 3D
a = np.array([[[1, 2, 3], [4, 5, 6]]])
# print(a[0][1][1])
# print(a[0][0][2])

b = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(b)
print(b.ndim)
print(b[1][0][1])

print(b[0][0][2])