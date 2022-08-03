import numpy as np

a = np.arange(1, 11)
print(a[2])
print(a[:])
print(a[2:])
print(a[7:])
print(a[:5])
print(a[3:7])
print(a[2:9])
print(a[2:9:2])

b = np.array([10, 30, 40, 20, 50])
print(b[1:4:2])

c = np.array([10, 30, 40, 45, 50, 80, 100, 150, 200])
print(c[::3])
