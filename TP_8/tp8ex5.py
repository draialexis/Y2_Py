import numpy as np

A = np.array([6, 2, 8, 0, 3, 0, 1, 8, 7, 4, 0, 3, 2, 6, 7, 0]).reshape((4, 4))
print("A=\n", A)
b = np.array([1, 2, 3, 4])  # .reshape((4, 1))
print("b=\n", b)

print('\n=============1)=============\n')

"""
A.X = b <=> A^(-1).A.X = A^(-1).b <=> X = A^(-1)
"""
A_in = np.linalg.inv(A)
X = A_in.dot(b)
print("X=\n", X)

print('\n=============2)=============\n')
"""
using solve()
"""
X = np.linalg.solve(A, b)
print("X\n", X)

print('\n=============3)=============\n')
"""
Cramer's Rule:
[ 2 -1 |.[ x | = [ 4 |
| 0 1  ].| y ]   | 2 ]

x = det(2 4
        0 2)
    --------
    det(2 -1
        0 1)

y = det(4 -1
        2 1)
    --------
    det(2 -1
        0 1)
"""
X = np.array([])
# will only work for square A matrices of size b.size?
for i in range(b.size):
    A1 = np.copy(A)
    A1[:, i] = b
    c = np.linalg.det(A1) / np.linalg.det(A)
    X = np.hstack((X, c))

print("X\n", X)
