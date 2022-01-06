import matplotlib.pyplot as plt
import numpy as np

## 1)
print('\n######1######\n')

def birthdays(n):
    res = np.random.randint(0, 364, n)
    return res


def close_30(l):
    l = sorted(l)
    streaks = [0]
    close = 0
    for i in range(len(l) - 1):
        if abs(l[i] - l[i+1])  <= 30:
            close += 1
        else:
            if close > 0:
                streaks.append(close)
                close = 0
    if close > 0:
        streaks.append(close)
    return max(streaks)

def evaluate_close(n, m):
    tries = 20000
    successes = 0
    for _ in range(tries):
        if close_30(birthdays(n)) >= m:
            successes += 1
    return (successes / tries) * 100

print("prob =", round(evaluate_close(5, 4), 3), "%")

## 2)
print('\n######2######\n')


def avg_intvl(l):
    res = 0
    l = sorted(l)
    for i in range(len(l) - 1):
        res += abs(l[i] - l[i+1])
    return res / len(l)

def evaluate_intvl(n):
    iters = 20000
    res = 0
    for _ in range(iters):
        res += avg_intvl(birthdays(n))
    return (res / iters)


print("moyenne =", round(evaluate_intvl(5), 3), "jours")


## 3)
print('\n######3######\n')


def max_intvl(l):
    res = abs(l[0] - l[1])
    l = sorted(l)
    for i in range(1, len(l) - 1):
        candidate = abs(l[i] - l[i+1])
        if candidate > res:
            res = candidate
    return res

def evaluate_max_intvl(n):
    iters = 20000
    res = 0
    for _ in range(iters):
        res += avg_intvl(birthdays(n))
    return (res / iters)

L = []

for i in range(20000):
    L.append(max_intvl(birthdays(5)))

plt.hist(L, bins=12, edgecolor='black')
plt.title("3) resultats sur 20 000 essais")
plt.figure()


## 4)
print('\n######4######\n')


# find how many times a specific outcome is present in the same spot in two series of throws
# size the sample size
# f the function used (die_throw, coin_flip...)
# n the number of throws in each series
def find_outcome_pair(size, f, n):
    tally = {'yes': 0, 'no': 0}

    for i in range(size):
        a = f(n)
        b = f(n)
        found_one = 0
        for i, item in enumerate(a):
            if item == b[i]:
                found_one = 1
                tally['yes'] += 1
        if found_one == 0:
            tally['no'] += 1

    for key in tally:
        tally[key] = tally[key] * 100 / size

    return tally

tally = find_outcome_pair(20000, birthdays, 30)

print("prob =", round(tally["yes"]), "%")


## 5)
print('\n######5######\n')

def find_outcome_pair_intvl(size, f, n_a, n_b):
    res = []
    for n in range(n_a, n_b+1):
        tally = {'yes': 0, 'no': 0}
        for i in range(size):
            a = f(n)
            b = f(n)
            found_one = 0
            for i, item in enumerate(a):
                if item == b[i]:
                    found_one = 1
                    tally['yes'] += 1
            if found_one == 0:
                tally['no'] += 1

        res.append(tally["yes"] * 100 / size)

    return res

x = np.linspace(20, 30, 11)
y = find_outcome_pair_intvl(2000, birthdays, 20, 30)

plt.plot(x, y)
plt.title("5) resultats en % sur 2000 essais chacun, pour des classes de 20 à 30")
plt.show()

print("la prob sera entre 20/365 et 30/365, soit environ 5% à 8.5%...")







