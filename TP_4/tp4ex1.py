import matplotlib.pyplot as plt
import numpy as np

def fibo(n):
    res = 0
    if n < 0:
        print('oh no no no')
        return -1
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        res += (fibo(n - 1) + fibo(n - 2))

    return res


def fibo_liste(n):
    res = []

    for i in range(0, n + 1):
        res.append(fibo(i))

    return res

L = fibo_liste(25)
plt.plot(L[5:])
plt.show()

plt.yscale('log')
plt.show()

# croissance exponentielle

