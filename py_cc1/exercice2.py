# Alexis DRAI - 22001161
# 08/11/2021

import matplotlib.pyplot as plt
import numpy as np

## 1)

def fibo(n):
    res = 0
    if n < 0:
        exit()
    if n == 0 or n == 1:
        return n
    else:
        res += (fibo(n - 1) + fibo(n - 2))

    return res

def fibo_liste(n):
    res = []

    for i in range(0, n):
        res.append(fibo(i))

    return res
print('ex2_1')
print(fibo_liste(11))

## 2)

cst = 4

def inv_mod(a):
    for i in range(1, cst):
        a_m = a % cst
        i_m = i % cst
        a_i_m = a_m * i_m % cst
        if a_i_m == 1:
            return i
    return 0

my_x = []
my_y = []

for n in range(10):

    if n == 0:
        x_prev = 0
        y_prev = 0
        my_x.append(0)
        my_y.append(0)
    else:
        if inv_mod(n) == 0:
            my_x.append(x_prev)
        elif inv_mod(n) == 1:
            my_x.append(x_prev + fibo(n-1))
        elif inv_mod(n) == 2:
            my_x.append(x_prev)
        elif inv_mod(n) == 3:
            my_x.append(x_prev - fibo(n-1))

print('ex2_2')
print('x:', my_x)
print('y (pas eu le temps):', my_y)


































