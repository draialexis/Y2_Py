#import numpy as np
from math import factorial

#1)

def inverse(L):
    return L[::-1]

L = [7, 3, 2, 5, 9]
print(L)
L = inverse(L)
print(L)

#2)

def dec(B):
    res = 0
    i = len(B) - 1
 #   B = inverse(B)

    for digit in B:
        res += pow(2, i) * digit
        #•print('+', pow(2, i), '*', digit, '=', pow(2, i) * digit)
        i -= 1

    return res

list1 = [1, 1, 0, 1] #13
print(list1, '(b10) =', dec(list1))

list2 = [1, 0, 1, 1, 1, 0, 0, 1] #185
print(list2, '(b10) =', dec(list2))

#3)

list3 = [1, 1, 0, 1, 1, 0, 0]
list4 = [1, 0, 1, 0, 1, 0, 1, 0]
print(list3, '+', list4, '=', (dec(list3) + dec(list4))) #like this?

#4)

def binaire(n):
    res = []
    digit = -1
    while n > 0:
        digit = n % 2
        res.insert(0,digit) #or "res.append(digit)"
        n = n // 2
    #or "res = inverse(res)"
    return res

num1 = 13
print(num1, '(b2) =', binaire(num1))
num2 = 278
print(num2, '(b2) =', binaire(num2))

#5)

print(list3, '+', list4, '=', binaire((dec(list3) + dec(list4)))) #like this?

#6)

print(factorial(50), '(b2) =', binaire(factorial(50)))
