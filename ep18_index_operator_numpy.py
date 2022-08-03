import numpy as np

# index operator 1D
a = np.arange(1, 10)
index = np.array([2, 4, 6, 8])
# print(index)
# print(a[index])
# print(a[1])
# print(a[[2, 4, 6, 8]])
# print(a[[0, 1]])
# print(a[0])


# index operator 2D
b = np.array([[1, 2, 3], [4, 5, 6, ], [7, 8, 9]])
# print(b[[0,2]])
# print(b[[0, 2], [2, 0]])
# print(b[[0, 2], [1]])

c = np.array([2, 3, 4])
# print(a[c])



d = a[[1, 4, 1, 4, 1, 4, 1, 4]]
# print(d)

e = np.array([[1, -2, 3], [4, -5, -6]])
print(e[e < 0])
print(e[e > 2])
print(e[e < 0]*-1)
print(e[e < 0]*2)
print(e[e < 0]*-2)
print(e[e < 0]**2)
