import numpy as np

a = np.array([1, 2, 3, 4, 5])
print(a)
print(a.shape)
print(a.ndim)
print(a.dtype)
print(a.size)

b = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(b)
print(b.shape)
print(b.ndim)
print(b.dtype)
print(b.size)

c = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
print(c.shape)
print(c.size)
print(c.itemsize)

d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]], dtype='complex')
print(d.dtype)
print(d.itemsize)
