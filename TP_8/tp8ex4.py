import numpy as np

A = np.array([[1, 2], [3, 4]])
print("A =\n", A)

B = np.array([[2, -1], [2, 7]])
print("B =\n", B)

C = np.array([[1, 1, 1, 1], [2, 2, 2, 2]])
print("C =\n", C)

x = np.array([[1, -2]])
x = x.reshape(2, )
print("x =\n", x)

z = np.array([7, 7])
z = z.reshape(2, )
print("z =\n", z)

print("A + B =\n", A + B)

print("A.B =\n", A.dot(B))

print("G = A 'x' B =\n", A * B)

print("A.C =\n", A.dot(C))

print("A.x =\n", A.dot(x))

print("10C =\n", C * 10)

print("z.C =\n", z.dot(C))

print("x + z =\n", x + z)

"""
buggy part vvv
"""
print("<x, z> =\n", np.cross(x, z))
