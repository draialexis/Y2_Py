import matplotlib.pyplot as plt
import numpy as np

print('\n===========1) & 2)==========\n')

N = 20
dom = np.linspace(-1 * np.pi, np.pi, N)
b = np.sin(dom)
print("b=\n", b)

L = np.ones((N, N))
for i in range(N):
    L[:, i] = pow(b, i)

print('\nL=\n', L)

a = np.linalg.solve(L, b)

print('\na=\n', a)

"""
N = 4:

L . a = b

| 1  0      0     0     |   | 0 |   | 0     |
| 1  -0.87  0.75  -0.65 | . | 1 | = | -0.87 |
| 1  0.87   0.75  0.65  |   | 0 |   | 0.87  |
| 1  0      0     0     |   | 0 |   | 0     |

"""

P = np.polyval(a[::-1], dom)
print("\n", P)
plt.plot(dom, b)
plt.plot(dom, P)
plt.figure()

print('\n=============3)=============\n')

x = np.linspace(-1 * (np.pi), np.pi, N)
y = np.sin(x)
k = len(x) - 1
P_ = np.polyfit(x, y, k)
print(P_)
plt.plot(x, y)
plt.plot(x, P_)
plt.show()
