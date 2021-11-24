import matplotlib.pyplot as plt
from numpy.random import randint

print('########1########')


def serie(n):
    L = randint(1, 7, n)
    return L


print(serie(100))

print('########2########')

print('############a####')

tally = {
    'yes': 0,
    'no': 0
}

"""
1/6 chances ; *4 => 4/6 chances (66.6%)
hy do I get 51.7% (4/7...)

"""

r = 200

for i in range(r):
    if 6 in serie(4):
        tally['yes'] += 1
    else:
        tally['no'] += 1

tally['yes'] = tally['yes'] * 100 / r
tally['no'] = tally['no'] * 100 / r

print(tally)
plt.bar(tally.keys(), tally.values(), color='g')
plt.figure()

print('############b####')

tally = {
    'yes': 0,
    'no': 0
}

r = 20000

for _ in range(r):
    A = serie(24)
    B = serie(24)
    found_one = 0
    for i, item in enumerate(A):
        if item == 6 and B[i] == 6:
            found_one = 1
            # print('A[', i, '] = B[', i, '] = ', item)
            tally['yes'] += 1
            # break;
    if found_one == 0:
        tally['no'] += 1

tally['yes'] = tally['yes'] * 100 / r
tally['no'] = tally['no'] * 100 / r

print(tally)
plt.bar(tally.keys(), tally.values(), color='g')
plt.show()
