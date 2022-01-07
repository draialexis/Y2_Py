import matplotlib.pyplot as plt
import numpy as np

n = 5

a = 0
b = n - 1

## 1)
print('\n######1######\n')

u = np.linspace(a, b, n)
v = np.linspace(b, a, n)

print('u =', u)
print('v =', v)

## 2)
print('\n######2######\n')

w = np.hstack((u, v))

print('w =', w)

## 3)
print('\n######3######\n')

A = np.zeros((w.size, w.size))
A[0, :] = A[-1, :] = A[:, 0] = A[:, -1] = w
print('A =\n', A)

## 4)
print('\n######4######\n')


def iteration(m):
    for i in range(1, w.size - 1):
        for j in range(1, w.size - 1):
            m[i, j] = (m[i - 1, j] + m[i + 1, j] + m[i, j - 1] + m[i, j + 1]) / 4


for _ in range(5):
    iteration(A)

plt.matshow(A)
plt.title("4) A, n=5, apres 5 appels a iteration")
plt.show()

## 5)
print('\n######5######\n')

for _ in range(1000):
    iteration(A)

plt.matshow(A)
plt.title("5) A, n=5, apres 1000 appels a iteration")
plt.show()

## 6)
print('\n######6######\n')

n = 30

u = np.linspace(a, b, n)
v = np.linspace(b, a, n)

w = np.hstack((u, v))

A = np.zeros((w.size, w.size))
A[0, :] = A[-1, :] = A[:, 0] = A[:, -1] = w

for _ in range(5):
    iteration(A)

plt.matshow(A)
plt.title("6) A, n=30, apres 5 appels a iteration")
plt.show()

for _ in range(1000):
    iteration(A)

plt.matshow(A)  # 10 ou 12 sec de temps d'execution (!)
plt.title("6) A, n=30, apres 1000 appels a iteration")
plt.show()
