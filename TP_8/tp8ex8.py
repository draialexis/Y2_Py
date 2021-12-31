import numpy as np

EPSILON = pow(2, -15)
eps = pow(10, -8)
print('\n=============1)=============\n')


# dom = np.linspace(-3, 3, 100)
# F = [f(i) for i in dom]
# F_p = [f_p(i) for i in dom]
# plt.plot(dom, F)
# plt.plot(dom, F_p)
# plt.axis("equal")
# plt.show()

def newt(f, df, x, eps):
    c = 0
    while abs(f(x)) > eps:
        c += 1
        print("\nc:", c)
        print("abs(f(x))=", abs(f(x)))
        if (abs(df(x)) > EPSILON):
            x = x - (f(x) / df(x))
        else:
            print("pick another x_0 to avoid division by 0")
            return None, None
        print("x_n = x_(n-1) - (f(x_(n-1)) / df(x_(n-1))) = ", x)

    return x, c


fun = lambda x: pow(x, 3) + 2 * pow(x, 2) + 1
fun_p = lambda x: 3 * pow(x, 2) + 4 * x

my_x, my_c = newt(fun, fun_p, 1, eps)
print('\n\nx=', my_x, ', c=', my_c)

print('\n=============2)=============\n')

fun = lambda x: np.sin(x) - np.log(x)
fun_p = lambda x: np.cos(x) - (1 / x)

my_x, my_c = newt(fun, fun_p, 1, eps)  # x_0 must be > 0
print('\n\nx=', my_x, ', c=', my_c)

fun = lambda x: 2 * x + 3 - pow(np.e, x)
fun_p = lambda x: 2 - np.e * x

my_x, my_c = newt(fun, fun_p, 1, eps)
print('\n\nx=', my_x, ', c=', my_c)

"""
looks like it converges faster sometimes
"""
