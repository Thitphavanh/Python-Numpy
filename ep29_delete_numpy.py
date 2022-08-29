import numpy as np


a = np.arange(1, 13)
# print(a)

# a = np.delete(a, 1)
# print(a)

# a = np.arange(1, 12)
# print(a)

a = np.arange(1, 13).reshape(4, 3)
# print(a)

# a = np.delete(a, 2, axis=0)
# print(a)

a = np.delete(a, 2, axis=0)
print(a)

a = np.delete(a, 0, axis=1)
print(a)