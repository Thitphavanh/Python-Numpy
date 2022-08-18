from tkinter import Y
import numpy as np

# index operator 1D
a = np.arange(1, 10)
# print(a)
# print(a+2)
# print(a+12)
# print(a-5)
# print(a*5)
# print(a**5)
# print(a%5)
# print(a/5)
print(a.shape)

b = np.arange(1, 5)
print(b.shape)

c = np.arange(1, 15)

x = np.array([[1, 2, 3], [4, 5, 6]])
print(x)


y = np.array([[7, 8, 9], [10, 11, 12]])
print(y)

print(x+y)
print(x-y)
print(x*y)
print(x**y)
print(x/y)
print(x % y)
print(x+[2])

z = np.array([1,2])
print(z.shape)