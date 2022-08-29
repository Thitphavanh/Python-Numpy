import numpy as np

# Array 1D
a = np.arange(1, 21)
# a = np.split(a, 5)
# print(a)
# a = np.split(a, 4)
# print(a)

# # Array 2D
a = a.reshape(5, 4)
print(a)

# a = np.hsplit(a, 4)
# print(a)

a = np.vsplit(a, 5)
print(a)