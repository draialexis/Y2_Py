import numpy as np
import matplotlib.pyplot as plt


def triangle(x, y, c):
    plt.plot([x, x + c, x + (c / 2), x], [y, y, y + (c * np.sqrt(3) / 2), y], color="b")


# 1)

triangle(0, 0, 0.5)
triangle(0.5, 0, 0.5)
triangle(0.25, 0.5 * (np.sqrt(3) / 2), 0.5)
plt.axis('equal')
plt.figure()


# 2)

def t2s(n, x, y, c):
    if n >= 1:
        triangle(x, y, c)
        triangle(x + c, y, c)
        triangle(x + c / 2, y + c * (np.sqrt(3) / 2), c)
        t2s(n - 1, x, y, c / 2)
        t2s(n - 1, x + c, y, c / 2)
        t2s(n - 1, x + c / 2, y + c * (np.sqrt(3) / 2), c / 2)


t2s(6, 0, 0, 0.5)
plt.axis('equal')
plt.show()
