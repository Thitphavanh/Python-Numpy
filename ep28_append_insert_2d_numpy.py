import numpy as np


# Array 2D
a = np.array([[1, 2], [3, 4]])
# print(a)

# a = np.insert(a, 1, 50, axis=0)
# print(a)

# a = np.insert(a, 1, 150, axis=1)
# print(a)

a = np.insert(a, 1, [150, 10], axis=0)
print(a)