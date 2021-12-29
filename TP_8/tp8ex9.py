import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

print('\n=============1)=============\n')

fun = lambda x: np.sin(x)

def check_intvl(a, b):
    if a == b:
        print("[", a, ",", b, "] is not a thing...")
        return None, None
    if a > b:
        print("[", a, ",", b, "] ? inverting poles...")
        a, b = b, a
    return a, b

def int_rect_g(f, a, b, n):
    a, b = check_intvl(a, b)
    y = f(np.linspace(a, b, n + 1))
    return (b-a)/n * sum(y[:-1])

should_be_1 = int_rect_g(fun, 0, np.pi/2, 100)
print(should_be_1)

def int_rect_d(f, a, b, n):
    a, b = check_intvl(a, b)
    y = f(np.linspace(a, b, n + 1))
    return (b-a)/n * sum(y[1:])

should_be_1 = int_rect_d(fun, 0, np.pi/2, 100)
print(should_be_1)

def int_trapz(f, a, b, n):
    a, b = check_intvl(a, b)
    y = f(np.linspace(a, b, n + 1))
    # return ((b-a)/(2*n)) * (sum(y[1:]) + sum(y[:-1]))
    return (int_rect_g(f, a, b, n) + int_rect_d(f, a, b, n)) / 2

should_be_1 = int_trapz(fun, 0, np.pi/2, 100)
print(should_be_1)

print('\n=============2)=============\n')

n = 1
fun_1 = lambda x: pow(np.e, np.sin(x))

for i in range(7):
    n *= 10
    area = int_rect_g(fun_1, -1 * np.pi, np.pi, n)
    print("fun_1 area at n =", n,":", area)
print('\n')

n = 1
fun_2 = lambda x: np.e * (-1 * pow(x, 2))

for i in range(7):
    n *= 10
    area = int_rect_d(fun_2, -10, 2, n)
    print("fun_2 area at n =", n,":", area)

"""
vidi, vici, veni
"""

print('\n=============3)=============\n')

print("fun_1 integral:", quad(fun_1, -1 * np.pi, np.pi))
print("fun_2 integral:", quad(fun_2, -10, 2))

"""
it's... less precise but faster than with n=10^7?
"""