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

y = np.array([3, 1, -0.5])
y = y.reshape(3, )
print("y =\n", y)

z = np.array([7, 7])
z = z.reshape(2, )
print("z =\n", z)

D = np.zeros((10, 20))
print("D =\n", D)

E = np.zeros((7, 7)) + 7
print("E =\n", E)

I = np.identity(8)
print("I =\n", I)

u = np.arange(1, 101, 1)
u = u.reshape(100, )
print("u =\n", u)

L = np.diag(np.arange(1, 101, 1))
print("L =\n", L)

M = np.diag(np.zeros(100) + 2) + np.diag(np.zeros(99) - 1, -1) + np.diag(np.zeros(99) - 1, +1)
print("M =\n", M)
