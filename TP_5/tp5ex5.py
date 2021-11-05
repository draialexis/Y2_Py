import sympy as sm
from sympy import limit, sqrt, oo, pprint, diff, integrate, log

sm.var('x a n')

# 1)

l1 = sqrt(x ** 2 + x) - sqrt(x ** 2 + 1)
pprint(l1)
print('lim(x->oo):')
pprint(limit(l1, x, oo))
print('')

l2 = (1 + a / (3 * n)) ** (2 * n)
pprint(l2)
print('lim(n->oo):')
pprint(limit(l2, n, oo))
print('')

# 2)

f = x / (1 + sqrt(x))

pprint(f)
print('integ(x)->')
f_i = integrate(f, x)
pprint(sm.simplify(f_i))
print('diff(x)->')
f_i_d = diff(f_i)
pprint(sm.factor(f_i_d))
print('')

g = 3 * x * sqrt(1 + x ** 2)

pprint(g)
print('integ(x)->')
g_i = integrate(g, x)
pprint(sm.simplify(g_i))
print('diff(x)->')
g_i_d = diff(g_i)
pprint(sm.simplify(g_i_d))
print('')

h = sqrt(log(x)) / x

pprint(h)
print('integ(x, 1, 2)->')
h_i = integrate(h, (x, 1, 2))
pprint(h_i)
print('~=')
print(h_i.evalf(20))
