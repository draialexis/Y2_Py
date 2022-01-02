import matplotlib.pyplot as plt
import numpy as np

# 1)

x_0 = 0.2


def ser(n, a):
    x = 0
    x_prev = x_0
    for i in range(n + 1):
        x = a * x_prev * (1 - x_prev)
        x_prev = x
    return x
    # return a * seq(n - 1) * (1 - seq(n - 1))


l1 = []
for i in range(201, 211):
    l1.append(ser(i, 2.1))

print(l1)

print('#1 the sequence converges towards 0.5238095238095238 when a = 2.1')

# 2)


l2 = []
for i in range(201, 211):
    l2.append(ser(i, 3.1))
# plt.plot(np.linspace(0, 1, 10), l2)
# plt.show()

print('#2 the sequence oscillates between 0.5570939072227653 and 0.7648948858499187 when a = 3.1')

# 3)

l3 = []
a_ = [3.46] * 10
for i in range(201, 211):
    l3.append(ser(i, 3.46))
# plt.scatter(a_, l3)
# plt.show()

print('#3 four points can be seen, now oscillating between 4 values at a = 3.46')

# 4)

l4 = []
a = np.arange(2.5, 4.01, 0.01)  # the last 0.1 won't be included
r = range(200, 301)
for i in a:
    for j in r:
        l4.append(ser(j, i))
    a_ = [i] * len(r)
    plt.scatter(a_, l4, color='r')
    l4 = []
plt.show()

print('#4 this looks a lot like a binary tree')
