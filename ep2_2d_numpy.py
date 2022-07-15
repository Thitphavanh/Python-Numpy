# Array 2D
import numpy as np
from pandas import array

# array 2D
array([1, 2, 3])
b = np.array([[1, 2, 3], [4, 5, 6]])
# print(b)
# print(b.ndim)

# list Array 2D
lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
c = np.array(lists)
# print(c)

# Tuple Array 2D
tuples=((1, 2, 3),(4, 5, 6),(7, 8, 9))
d = np.array(tuples)
print(d)
