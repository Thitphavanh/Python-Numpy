import numpy as np


# Array 1D
a = np.array([1, 2, 3, 4, 5])
# print(a)
a = np.append(a, 150)
print(a)
a = np.insert(a, 1, 100)
print(a)

a = np.insert(a, (0, 2), 200)
print(a)
