import numpy as np


a = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
# print(a.reshape((2, 5)))
a.resize((2, 5))
print(a)

b = a.reshape((2, 5))
# print(b)


