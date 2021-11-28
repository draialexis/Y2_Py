import numpy as np
import matplotlib.pyplot as plt
from numpy.random import rand

print('########1########')

s_1 = 5000


def bern(a, b, p):
    if rand() <= p:
        return b
    else:
        return a


def draw_walk(s):
    steps = [(bern(-1, 1, 0.5)) for _ in range(s)]
    walk = np.cumsum(steps)
    x = np.linspace(0, s, s)
    plt.plot(walk, x)


draw_walk(s_1)
plt.ylabel("0 to r")
plt.xlabel("left to right")
plt.title('"drunk walk", from (0, 0) to (0, s)')
plt.figure()

print('########2########')

r = 500
s_2 = 500

for i in range(r):
    draw_walk(s_2)

plt.ylabel("0 to r")
plt.xlabel("left to right")
plt.title('500 "drunk walks", from (0, 0) to (0, s)')
plt.figure()

print('########3########')

r = 20000
s_3 = 100
positions = []
for i in range(r):
    steps = [(bern(-1, 1, 0.5)) for _ in range(s_3)]
    walk = np.cumsum(steps)
    positions.append(walk[-1])

my_bins = [(i - 0.5) for i in range(-50, 51)]
# -100.5->-99.5 (ie -100), -99.5->-98.5, etc. 201 values counting 0, so "up to 202"
# ...
# except it's gonna be a bell curve, so let's not even look at the edges (just -50 -> +50)

plt.hist(positions, bins=my_bins, edgecolor='black', density=True)  # not "normed=1" (deprecated)

print('########4########')


def formula(x, sigma):
    return (1 / (sigma * np.sqrt(2 * np.pi))) * np.exp(-(pow(x, 2)) / (2 * pow(sigma, 2)))


# seems top work better for sigma = 5... what did I do wrong?


ys = [(formula(i, 10)) for i in range(-50, 51)]
plt.plot(np.linspace(-50, 50, 101), ys)
plt.show()
