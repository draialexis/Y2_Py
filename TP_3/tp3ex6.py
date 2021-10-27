import numpy as np
import matplotlib.pyplot as plt

def triangle(x, y, c):
    plt.fill([x, x+c, x+(c/2)], [y, y, y+(c*np.sqrt(3)/2)], color="b")

# 1)

#triangle(0, 0, 0.5)
#triangle(0.5, 0, 0.5)
#triangle(0.25, 0.5*(np.sqrt(3)/2), 0.5)
#plt.axis('equal')
#plt.show()

# 2)

def t2s(n, x, y, c):
    if n >= 1 :
        plt.plot([x, x+c, x+(c/2), x], [y, y, y+(c*np.sqrt(3)/2), y], color="g")
        new_x = x+c
        plt.plot([new_x, new_x+c, new_x+(c/2), new_x], [y, y, y+(c*np.sqrt(3)/2), y], color="g")
        new_x /= 2
        new_y = y+(c*np.sqrt(3)/2)
        plt.plot([new_x, new_x+c, new_x+(c/2), new_x], [new_y, new_y, new_y+(c*np.sqrt(3)/2), new_y], color="g")
        return t2s(n-1, x/2, y/2, c/2)


    plt.axis('equal')
    plt.show()

t2s(6, 0, 0, 1)