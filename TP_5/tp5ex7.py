import sympy as sm
from sympy import pprint, integrate

sm.var('x n a')

# 1)

f = (x ** (n - 1)) / (a + x)
print('f =')
pprint(f)
v = integrate(f, (x, 0, 1))
print('\ninteg(f[0,1]) =')
pprint(v)

# integ(f[0,1]) = ...wat.

# 2)

f = f.subs(n, 40)
print('f =')
pprint(f)
v = integrate(f, (x, 0, 1))
print('\ninteg(f[0,1], n:40) =')
pprint(v)

# 3)

v = v.subs(a, 3)
print('\ninteg(f[0,1], n:40, a:3) =')
pprint(v)

# 4)

print(v.evalf(20))

# our result from tp2ex2 was pretty close, this is better obviously
