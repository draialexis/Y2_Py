# from time import time
# from numpy.random import rand
# # use np.random.randint to get several random ints
# from random import randint
# from scipy.integrate import quad
#
#
import matplotlib.pyplot as plt
import numpy as np

# import math as m
# import sympy as sm

"""
TP2
"""


def dec_from_binlist(b):
    res = 0
    for i, digit in enumerate(b[::-1]):
        res += pow(2, i) * digit
    return res


def binlist_from_dec(n):
    res = []
    while n > 0:
        res.append(n % 2)
        n = n // 2
    return res[::-1]


def gcd(a, b):
    while b != 0:
        r = a % b
        a = b
        b = r
    return a


def farey(n):
    res = [0]
    # print('0 / 1')
    for i in range(1, n + 1):
        j = n
        while j > 0:
            if gcd(i, j) == 1 and i < j:
                # print(i, '/', j)
                res.append(i / j)
            j -= 1
    # print('1 / 1')
    res.append(1)
    return res


"""
TP3
"""


def encode_one(lt):
    switcher = {
        'A': 0,
        'B': 1,
        'C': 2,
        'D': 3,
        'E': 4,
        'F': 5,
        'G': 6,
        'H': 7,
        'I': 8,
        'J': 9,
        'K': 10,
        'L': 11,
        'M': 12,
        'N': 13,
        'O': 14,
        'P': 15,
        'Q': 16,
        'R': 17,
        'S': 18,
        'T': 19,
        'U': 20,
        'V': 21,
        'W': 22,
        'X': 23,
        'Y': 24,
        'Z': 25,
        ' ': ' ',
    }
    return switcher.get(lt, '#')


def decode_one(c):
    switcher = {
        0: 'A',
        1: 'B',
        2: 'C',
        3: 'D',
        4: 'E',
        5: 'F',
        6: 'G',
        7: 'H',
        8: 'I',
        9: 'J',
        10: 'K',
        11: 'L',
        12: 'M',
        13: 'N',
        14: 'O',
        15: 'P',
        16: 'Q',
        17: 'R',
        18: 'S',
        19: 'T',
        20: 'U',
        21: 'V',
        22: 'W',
        23: 'X',
        24: 'Y',
        25: 'Z',
        ' ': ' ',
    }
    return switcher.get(c, '#')


def encode(str_p):
    return list(map(encode_one, str_p))


def decode(code):
    return "".join(list(map(decode_one, code)))


def cesar(string, d, is_decypher):
    if is_decypher:
        d = -1 * d
    nums = encode(string)
    nums_delta = []
    for num in nums:
        if isinstance(num, int):
            nums_delta.append((num + d) % 26)
        elif num == ' ':
            nums_delta.append(num)

    res = decode(nums_delta)
    return res


def inverse(a, cst):
    for i in range(1, cst):
        a_m = a % cst
        i_m = i % cst
        a_i_m = a_m * i_m % cst
        if a_i_m == 1:
            return i
    return 0


def affine(string, a, b, is_decypher):
    cst = 26
    nums = encode(string)
    nums_delta = []
    for num in nums:
        if isinstance(num, int):

            if is_decypher:
                # print('num:', num)
                # print('num-b:', num - b)
                # print('(num-b)*inverse(a):', (num - b) * inverse(a, 26))
                # print('((num-b)*inverse(a))%26:', ((num - b) * inverse(a, 26)) % 26)
                nums_delta.append(((num - b) * inverse(a, cst)) % cst)
            else:
                # print('num:', num)
                # print('alpha:', (a * num + b))
                # print('alpha modulo 26:', (a * num + b) % 26)
                nums_delta.append((a * num + b) % cst)

        elif num == ' ':
            nums_delta.append(num)

    return decode(nums_delta)


def tri(x, y, c):
    plt.plot([x, x + c, x + (c / 2), x], [y, y, y + (c * np.sqrt(3) / 2), y], color="b")


def serpinski_tri(n, x, y, c):
    if n >= 1:
        tri(x, y, c)
        tri(x + c, y, c)
        tri(x + c / 2, y + c * (np.sqrt(3) / 2), c)
        serpinski_tri(n - 1, x, y, c / 2)
        serpinski_tri(n - 1, x + c, y, c / 2)
        serpinski_tri(n - 1, x + c / 2, y + c * (np.sqrt(3) / 2), c / 2)


"""
TP4
"""


def fibo(n):
    res = 0
    if n < 0:
        print('oh no no no')
        return None
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        res += (fibo(n - 1) + fibo(n - 2))
    return res


# tgt = f'(x_a) * (x - x_a) + f(x_a)

"""
TP5
"""

"""
BONUS
"""


def polygone(n, is_inscribed=True):
    # setting up the true circle constant jus cuz
    tau = 2 * np.pi
    # setting up a unit circle
    x = np.linspace(0, tau)
    plt.plot(np.cos(x), np.sin(x))

    cst = tau / n  # the absolute angle covered by each slice
    coeff = 1  # the coefficient by which we find coordinates of vertices, important if is_inscribed == False
    if not is_inscribed:
        coeff = 1 / np.cos(tau / (2 * n))

    x = []
    y = []
    for i in range(n):
        theta = i * cst  # the angle of a specific slice relative to the origin
        # the coordinates of the vertices
        x.append(coeff * np.cos(theta))
        y.append(coeff * np.sin(theta))

    # closing the circuit
    x.append(x[0])
    y.append(y[0])
    plt.plot(x, y)
    plt.axis('equal')
    plt.show()
