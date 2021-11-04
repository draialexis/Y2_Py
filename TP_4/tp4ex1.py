import matplotlib.pyplot as plt
from math import sqrt


def fibo(n):
    res = 0
    if n < 0:
        print('oh no no no')
        exit()
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        res += (fibo(n - 1) + fibo(n - 2))
    return res


def fibo_approx(n):
    if n < 0:
        print('oh no no no')
        exit()
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n <= 5:
        return fibo(n - 2) + fibo(n - 1)
    else:
        return fibo(n - 1) * ((1 + sqrt(5)) / 2)


def fibo_approx_liste(n):
    res = []

    for i in range(0, n + 1):
        res.append(fibo_approx(i))

    return res


L = fibo_approx_liste(25)
plt.plot(L[5:], c='g')
plt.figure()

plt.plot(L[5:], c='g')
plt.yscale('log')
plt.figure()


def fibo_liste(n):
    res = []

    for i in range(0, n + 1):
        res.append(fibo(i))

    return res


L = fibo_liste(25)
plt.plot(L[5:], c='b')
plt.figure()

plt.plot(L[5:], c='b')
plt.yscale('log')
plt.show()
