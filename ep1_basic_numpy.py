import numpy as np

# array 0D
arrays = np.array(1)
print(arrays)

arrays = np.array(2)
print(arrays)

# array 1D
arrays.ndim
a = np.array([1, 2, 3])
print(a)
print(a.ndim)

# list
lists = [1, 2, 3, 4]
b = np.array(lists)
print(b)

# tuble change to array
tubles = (1, 2, 3, 4, 5, 6)
c = np.array(tubles)
print(c)

d = np.array((1, 2, 3, 4))
print(d)