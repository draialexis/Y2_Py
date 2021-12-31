import matplotlib.pyplot as plt

a = [0, 0]
b = [2, 0]
c = [1, 1]

for i in range(6):
    plt.plot([a[0], b[0], c[0], a[0]], [a[1], b[1], c[1], a[1]])
    prev_a = a.copy()
    a = [(a[0] + b[0]) / 2, (a[1] + b[1]) / 2]
    b = [(b[0] + c[0]) / 2, (b[1] + c[1]) / 2]
    c = [(c[0] + prev_a[0]) / 2, (c[1] + prev_a[1]) / 2]
plt.show()
