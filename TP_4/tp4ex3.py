import numpy as np
import matplotlib.pyplot as plt

# 1) & 2)

t = np.arange(0.3, 2, 0.2)
x = np.linspace(0, 1, 100)
for i in range(len(t)):
    y = pow(x, t[i])
    my_str = "x^" + str(round(t[i], 2))
    plt.plot(x, y, label=my_str)
plt.legend(loc=0)
plt.title("f_t: x -> x^t, x€[0,1]")
plt.axis('equal')
plt.grid()
plt.figure()

# 3) & 4)

t_ = np.arange(0.4, 3, 0.1)
x_ = np.linspace(0, 1, 100)
j = 1
for i in range(len(t_)):
    y_ = pow(x_, t_[i])
    my_str = "x^" + str(round(t_[i], 2))
    plt.plot(x_, y_, color=plt.cm.hsv(j))
    j += 1
plt.title("f_t: x -> x^t, x€[0,1]")
plt.axis('equal')
plt.grid()
plt.show()


