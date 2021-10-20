import matplotlib.pyplot as plt
import numpy as np

a = [0, 0]
b = [2, 0]
c = [1, 1]
x = []
y = []

for i in range (0, 7):
    x.append(a[0])
    x.append(b[0])
    x.append(c[0])
    y.append(a[1])
    y.append(b[1])
    y.append(c[1])
    plt.plot(x, y)
    prev_a = a.copy()
    prev_b = b.copy()
    prev_c = c.copy()
    a[0] = (prev_b[0] + prev_a[0]) / 2
    b[0] = (prev_c[0] + prev_b[0]) / 2
    c[0] = (prev_a[0] + prev_c[0]) / 2


plt.show()