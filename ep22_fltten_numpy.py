# flatten ການເຮັດໃຫ້ array ຫຼາຍມິຕິແປງເປັນ1ມິຕິ
import numpy as np

a = np.array([[0, 1], [2, 3], [4, 5], [6, 7], [8, 9]])
# print(a)
# print(a.flatten())
# print(a)

b = a.flatten()
# print(b)
b[0] = 5
# print(b)

a.ravel()
c = a.ravel()
print(c)
c[0] = 5
print(c)
print(a)
