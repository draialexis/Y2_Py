import numpy as np
import sympy as sm
"""
somme des chiffres de 2013!
"""

def fact(n):
    if (n < 0):
        print('positive ints only')
        return -1
    res = 1
    for i in range (2, n + 1):
        res *= i
    return res

def sum_digits(n):
    res = 0
    while n > 0:
        res += n % 10
        n = n // 10
    return res


print(sum_digits(fact(2013)))

"""
sum_digits(fact(2013)) = 24021
"""
