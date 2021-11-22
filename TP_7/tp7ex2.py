import numpy as np
import matplotlib.pyplot as plt
from numpy.random import randint

# 1) & 2)

def pf():
    return randint(0, 2, 100)

def in_row(l):
    streaks = [0]
    in_row = 0
    for i in range(len(l)):
        if l[i] == 1:
            in_row += 1
        else:
            if in_row > 0:
                streaks.append(in_row)
            in_row = 0
    return max(streaks)

probs = {
    3: 0,
    4: 0,
    5: 0,
    6: 0,
    7: 0,
    8: 0,
}

tries = 20000
for _ in range(tries):
    throws = pf()
    max_streak = in_row(throws)
    for key in probs:
        if max_streak >= key:
            probs[key] += 1

print(probs)

plt.bar(probs.keys(), probs.values(), color='g')
plt.show()
