import numpy as np

# Array 1D
a = np.array([2161, 20, 302, 40, 515, 1566])
# print(a)
# print(a.sum())
# print(a.prod())
# print(a.mean())
# print(a.min())
# print(a.max())
# print(a.argmax())
# print(a.argmin())

# Array 2D
b = np.array([[2161, 20, 302], [40, 515, 1566], [40, 515, 1506]])
print(b)
print(np.min(b, axis=1))
print(np.min(b, axis=0))
print(np.max(b, axis=1))
print(np.max(b, axis=0))
