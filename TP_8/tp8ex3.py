import numpy as np
from numpy.linalg import matrix_power

print('\n=============1)=============\n')

A = np.array([[1, 2], [3, 4]])
print("A =\n", A)

B = np.array([[2, -1], [2, 7]])
print("B =\n", B)

C = np.array([[1, 1, 1, 1], [2, 2, 2, 2]])
print("C =\n", C)

x = np.array([1, -2])
# x.reshape(2, 1)
print("x =\n", x)

y = np.array([3, 1, -0.5])
# y.reshape(1, 3)
print("y =\n", y)

z = np.array([7, 7])
# z.reshape(1, 2)
print("z =\n", z)

D = np.zeros((10, 20))
print("D =\n", D)

E = np.zeros((7, 7)) + 7
print("E =\n", E)

I = np.identity(8)
print("I =\n", I)

u = np.arange(1, 101, 1)
print("u =\n", u)

L = np.diag(np.arange(1, 101, 1))
print("L =\n", L)

M = np.diag(np.zeros(100) + 2)
M += np.diag(np.zeros(99) - 1, -1)
M += np.diag(np.zeros(99) - 1, +1)
print("M =\n", M)

print('\n=============2)=============\n')

print("A + B =\n", A + B)

print("A.B =\n", A.dot(B))

print("G = A 'x' B =\n", A * B)

print("A.C =\n", A.dot(C))

print("A.x =\n", A.dot(x))

print("10C =\n", C * 10)

print("z.C =\n", z.dot(C))

print("x + z =\n", x + z)

print("<x, z> =\n", x.dot(z))

print('\n=============3)=============\n')

"""
Modier la matrice A en remplacant l'element 4 par 0. Remplacer la deuxieme ligne de la matrice C par le vecteur 4 3 2 1. A partir de la matrice C ainsi obtenue, creer une nouvelle matrice F€M_2(R) contenant les deux premieres colonnes de C.
"""
A[1, 1] = 0
print("A =\n", A)

C[1,:] = np.array([4, 3, 2, 1])
print("C =\n", C)

print('\n=============4)=============\n')

"""
Calculer et afficher la puissance 10 de A. Proposer une solution en utilisant une boucle for. Comparer au resultat obtenu a l'aide de la fonction matrix_power du module numpy.linalg.
"""
A_pow10_for = A
for i in range(2, 11):
    A_pow10_for = A_pow10_for.dot(A)
    # print("A_pow", i, "_for =\n", A_pow10_for)


print("A_pow10_for =\n", A_pow10_for)

A_pow10_mp = matrix_power(A, 10)
print("A_pow10_mp =\n", A_pow10_mp)

