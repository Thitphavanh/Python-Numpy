import numpy as np

a = np.array([1, 2, 3, 4, 5, 6])
# print(a.dtype)
a = np.array([1, 2, 3, 4, 5, 6], dtype='int')
# print(a.dtype)
a = np.array([1, 2, 3, 4, 5, 6], dtype='float')
# print(a.dtype)
# print(a)

a = np.array([1, 2, 3, 4, 5, 6], dtype='complex')
print(a.dtype)
print(a)

b = np.array([[1, 2, 3], [4, 5, 6]], dtype='float')
print(b.dtype)
print(b)
