# from time import time
# # use np.random.randint to get several random ints
# from random import randint
# from scipy.integrate import quad
#
#
import matplotlib.pyplot as plt
import numpy as np
from numpy.random import rand

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


def encode_one(c):
    switcher = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9, 'K': 10, 'L': 11,
                'M': 12, 'N': 13, 'O': 14, 'P': 15, 'Q': 16, 'R': 17, 'S': 18, 'T': 19, 'U': 20, 'V': 21, 'W': 22,
                'X': 23, 'Y': 24, 'Z': 25, ' ': ' '}
    return switcher.get(c, '#')


def decode_one(c):
    switcher = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H', 8: 'I', 9: 'J', 10: 'K', 11: 'L',
                12: 'M', 13: 'N', 14: 'O', 15: 'P', 16: 'Q', 17: 'R', 18: 'S', 19: 'T', 20: 'U', 21: 'V', 22: 'W',
                23: 'X', 24: 'Y', 25: 'Z', ' ': ' '}
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


def inverse_mod(a, cst):
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
                nums_delta.append(((num - b) * inverse_mod(a, cst)) % cst)
            else:
                # print('num:', num)
                # print('alpha:', (a * num + b))
                # print('alpha modulo 26:', (a * num + b) % 26)
                nums_delta.append((a * num + b) % cst)

        elif num == ' ':
            nums_delta.append(num)

    return decode(nums_delta)


def tri(x_0, y_0, length):
    plt.plot([x_0, x_0 + length, x_0 + (length / 2), x_0],
             [y_0, y_0, y_0 + (length * np.sqrt(3) / 2), y_0],
             color="b")


def serpinski_tri(n, x_0, y_0, length):
    if n >= 1:
        tri(x_0, y_0, length)
        tri(x_0 + length, y_0, length)
        tri(x_0 + (length / 2), y_0 + length * (np.sqrt(3) / 2), length)
        n -= 1
        serpinski_tri(n, x_0, y_0, (length / 2))
        serpinski_tri(n, x_0 + length, y_0, (length / 2))
        serpinski_tri(n, x_0 + (length / 2), y_0 + length * (np.sqrt(3) / 2), (length / 2))


# serpinski_tri(6, 0, 0, 1)
# plt.axis('equal')
# plt.show()

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


"""
TP7
"""


# returns a list of outcomes from n coin flips
def coin_flips(n):
    return np.random.randint(0, 2, n)


# returns a list of outcomes from n die throws
def die_throws(n):
    return np.random.randint(1, 7, n)


# returns the size of the biggest streak from a list of outcomes from some coin flips
def max_streak(l):
    streaks = [0]
    streak = 0
    for i in range(len(l)):
        if l[i] == 1:  # we chose to interpret that '1' means 'tails'
            streak += 1
        else:
            if streak > 0:
                streaks.append(streak)
                streak = 0
    return max(streaks)


# size the size of sample, n the number of throws in one sequence, probs a dictionary of monitored outcomes
def max_streak_probs(size, n, probs):
    for _ in range(size):
        max_streak_inst = max_streak(coin_flips(n))
        for key in probs:
            if max_streak_inst >= key:
                probs[key] += 1

    for key in probs:
        probs[key] = probs[key] * 100 / size


# plt.bar(probs.keys(), probs.values(), color='g')
# plt.show()


def bern(a, b, p):
    if rand() <= p:
        return b
    return a


# find if a specific outcome is present at least once in a series of throws
# size the sample size
# f the function used (die_throw, coin_flip...)
# x the investigated outcome
# n the number of throws in each series
def find_outcome_one(size, f, x, n):
    tally = {'yes': 0, 'no': 0}

    for i in range(size):
        nums = f(n)
        found_one = 0
        for num in nums:
            if num == x:
                tally['yes'] += 1
                found_one = 1
                break
        if found_one == 0:
            tally['no'] += 1

    for key in tally:
        tally[key] = tally[key] * 100 / size

    return tally


# tally = find_outcome_one(20000, coin_flips, 1, 3)
# plt.bar(tally.keys(), tally.values(), color='g')
# plt.show()

# find how many times a specific outcome is present in the same spot in two series of throws
# size the sample size
# f the function used (die_throw, coin_flip...)
# x the investigated outcome
# n the number of throws in each series
def find_outcome_pair(size, f, x, n):
    tally = {'yes': 0, 'no': 0}

    for i in range(size):
        a = f(n)
        b = f(n)
        found_one = 0
        for i, item in enumerate(a):
            if item == x and b[i] == x:
                found_one = 1
                tally['yes'] += 1
        if found_one == 0:
            tally['no'] += 1

    for key in tally:
        tally[key] = tally[key] * 100 / size

    return tally


def draw_walk(s):
    steps = [(bern(-1, 1, 0.5)) for _ in range(s)]
    x = np.cumsum(steps)
    y = np.linspace(0, s, s)
    plt.plot(x, y)


def one_step():
    x = rand()
    if x < 0.25:
        return np.array([1, 0])
    elif x < 0.5:
        return np.array([0, 1])
    elif x < 0.75:
        return np.array([-1, 0])
    else:
        return np.array([0, -1])


def marche_2d(n):
    xs = [0]
    ys = [0]
    pos = np.array([0, 0])
    plt.scatter(xs, ys, s=50, color='r')
    for i in range(1, n):
        pos = pos + one_step()
        xs.append(pos[0])
        ys.append(pos[1])
    plt.plot(xs, ys, color='b')
    plt.scatter(xs[-1], ys[-1], s=50, color='g')
    plt.axis('equal')
    plt.legend("nda")
    plt.show()


"""
TP8
"""


def serp_carp(d):
    a = np.array([[1, 1, 1], [1, 0, 1], [1, 1, 1]])  # lvl1

    for k in range(1, d + 1):  # start from 1, stop at 6
        a = np.vstack((a, a, a))
        a = np.hstack((a, a, a))
        n, dmp = a.shape
        n = int(n / 3)
        for i in range(n, n * 2):
            for j in range(n, n * 2):
                # print("a[", i, "," , j, "]")
                a[i, j] = 0

    plt.matshow(a, cmap="Greys")
    plt.show()


def dicho(f, a, b, eps):
    if a == b:  # interval can't be nothing
        print("[", a, ",", b, "] is not a thing...")
        return None
    if a > b:  # interval shouldn't be [b, a]
        a, b = b, a
    m = (a + b) / 2
    c = 0
    while abs(f(m)) > eps:
        c += 1
        print("\nc:", c)
        print("[a, b] = [", a, ",", b, "]")
        print("m = (a + b) / 2 = ", m)
        print("abs(f(m))=", abs(f(m)))
        if f(a) * f(m) < 0:  # sign changed between a and m
            b = m  # new upper bound is m: midpoint
        elif f(b) * f(m) < 0:
            a = m
        else:
            print("sign doesn't change in [", a, ",", b, "]...")
            return None

        if (c > 100):  # arbitrary, could be dynamic or chosen by input
            print("can't find it...")
            return None
        m = (a + b) / 2

    print("\n\n[a, b] = [", a, ",", b, "]")
    print("abs(f(m))=", abs(f(m)))
    return m


# print('dicho(f, 0.1, 4, pow(10, -8)) =', dicho(lambda x: np.sin(x) - np.log(x), 0.1, 4, epsilon))

def newt(f, df, x, eps):
    c = 0
    while abs(f(x)) > eps:
        c += 1
        print("\nc:", c)
        print("abs(f(x))=", abs(f(x)))
        if abs(df(x)) > pow(2, -15):
            x = x - (f(x) / df(x))
        else:
            print("pick another x_0 to avoid division by 0")
            return None, None
        print("x_n = x_(n-1) - (f(x_(n-1)) / df(x_(n-1))) = ", x)

    return x, c


# my_x, my_c = newt(lambda x: pow(x, 3) + 2 * pow(x, 2) + 1, lambda x: 3 * pow(x, 2) + 4 * x, 1, my_eps)
# print('\n\n:::::::::::x=', my_x, ', c=', my_c, ':::::::::::')


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
    return (b - a) / n * sum(y[:-1])


def int_rect_d(f, a, b, n):
    a, b = check_intvl(a, b)
    y = f(np.linspace(a, b, n + 1))
    return (b - a) / n * sum(y[1:])


def int_trapz(f, a, b, n):
    a, b = check_intvl(a, b)
    y = f(np.linspace(a, b, n + 1))
    # return ((b-a)/(2*n)) * (sum(y[1:]) + sum(y[:-1]))
    return (int_rect_g(f, a, b, n) + int_rect_d(f, a, b, n)) / 2


# should_be_1 = int_trapz(lambda x: np.sin(x), 0, np.pi / 2, 100)
# print(should_be_1)


"""
BONUS
"""


def tangent(foo, x):
    # or use sympy and tgt = f'(x_a) * (x - x_a) + f(x_a)
    h = 1e-5
    a = (foo(x + h) - foo(x - h)) / (2 * h)

    b = foo(x) - (x * a)
    return a, b


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
