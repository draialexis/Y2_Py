import matplotlib.pyplot as plt
from numpy.random import randint

print('########1########')


def serie(n):
    L = randint(1, 7, size=n)
    return L


print(serie(10))

print('########2########')

print('############a####')

r = 20000

tally = {
    'yes': 0,
    'no': 0
}

for i in range(r):
    nums = serie(4)
    found_one = 0
    for num in nums:
        if num == 6:
            tally['yes'] += 1
            found_one = 1
            break
    if found_one == 0:
        tally['no'] += 1

tally['yes'] = tally['yes'] * 100 / r
tally['no'] = tally['no'] * 100 / r

print(tally)
plt.bar(tally.keys(), tally.values(), color='g')
plt.show()

"""
1/6 chances ; *4 => 2/3 chances (66.7%)
why do I get 51.7% (4/7...)?
probably linked to the fact that we look for 'at least' one 6:
we're not looking at all the throws, we're skipping some 6s
"""

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
            tally['yes'] += 1
    if found_one == 0:
        tally['no'] += 1

tally['yes'] = tally['yes'] * 100 / r
tally['no'] = tally['no'] * 100 / r

print(tally)
plt.bar(tally.keys(), tally.values(), color='b')
plt.show()

"""
1/36 chances (2.7%) ; *24 => 2/3 chances (66.7%)
we can get 66.7% if we count every time a double 6 occurs.
but if we do that and we don't count every time it does not occur, 
the total is above 100%. The instructions don't say 'at least'...
If we do compare 'yes' to 'no' for every double throw, then doing series of 24
is pointless, and we can just do one series of 20000 or so.
We will find 2.7% likelihood.
"""
