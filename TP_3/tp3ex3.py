from TP_2 import tp2ex5 as p
import tp3ex1 as prv

A = [0,
     1,
     2,
     3,
     4,
     5,
     6,
     7,
     8,
     9,
     10,
     11,
     12,
     13,
     14,
     15,
     16,
     17,
     18,
     19,
     20,
     21,
     22,
     23,
     24,
     25]


# "Supposons que 'a' est premier avec 26" -> pgcd(a, 26) = 1

# 1)

# for i in A:
#     res = p.pgcd(i, 26)
#     if res == 1:
#         print(i, 'is coprime with 26')


# 2)
# au lieu d'appliquer un decalage d a chaque lettre
# codee f(n) = n+d % 26 (n € [0; 25]),
# on applique une fonction affine
# f(n) = an+b % 26
# (pour une valeur admissible de a).

def affine(string, a, b):
    nums = prv.encode(string)
    if not p.pgcd(a, 26) == 1:
        print(p.pgcd(a, 26))
        print("'a' € [0, 25] must be coprime with 26")
        for i in A:
            res = p.pgcd(i, 26)
            if res == 1:
                print(i, 'is coprime with 26')

    nums_delta = []
    for num in nums:
        if isinstance(num, int):
            nums_delta.append((a * num + b) % 26)
        elif num == ' ':
            nums_delta.append(num)

    res = prv.decode(nums_delta)
    return res


# my_string = 'KILL ME NOW'
# print(affine(my_string, 25, 7))


# 3)

# print(1 % 26)
# 1 % 26 is a constant : 1
# a' * a = 1 => a' = 1 / a

# a' * a = 1 (mod 26)
# that's just asking "what a' * a will give you 1 when it's mod 26
# a' * a % 26 = 1

# a' = x
# a = 17
# %43 = %26

def gcd(a, b):
    if a < b:
        a, b = b, a
    while b != 0:
        r = a % b
        a = b
        b = r
    return a


my_a = gcd(43, 17)
my_b = gcd(17, 43)

# if gcd == 1...


# def modinv(a, m):
#     g, x, y = pgcd(a, m)
#     if g != 1:
#         print('modular inverse does not exist')
#         return
#     else:
#         return x % m


# print(modinv(17, 43))


# def xgcd(a, b):
#     prevx, x = 1, 0
#     prevy, y = 0, 1
#     while b:
#         q = a / b
#         x, prevx = prevx - q * x, x
#         y, prevy = prevy - q * y, y
#         a, b = b, a % b
#     return a, prevx, prevy
