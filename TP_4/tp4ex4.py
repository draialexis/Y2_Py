import matplotlib.pyplot as plt
import numpy as np

my_x = np.linspace(0.003906, 10, 256)
my_y = 1/my_x

def y_tan(x0, x) :
    return  (-1 / (x0**2)) * (x - x0) + (1 / x0)

my_y_t = y_tan(2, my_x)

plt.plot(my_x, my_y)
plt.plot(my_x, my_y_t)
plt.axis('equal')
plt.show()