# Array 1D index
import numpy as np
from pandas import array

# array 1D
a = np.array([1, 2, 3, 4, 5, 6])
print(a[3])
print(a[3]+a[4])
print(a[-1])
a[1] = 100
print(a)

b = np.array([105, 512, 3152, 4554, 5123, 64857])
print(b[2])
print(b[-2])
