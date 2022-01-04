import sympy as sm
from sympy import sqrt, pprint, diff, integrate, log, simplify, factor

sm.var('x')
lo = 0
hi = 1

f = (x * log(sqrt(x ** 2 + 3))) / sqrt(x ** 2 + 3)
pprint(f)
f = simplify(f)
print('\nf, simplified:')
pprint(f)

# from console output, find u and v'
# (the plan is to use integ(u*v') = u * v - integ (u'*v)
u = log(x ** 2 + 3)
v_ = x / (2 * sqrt(x ** 2 + 3))
print('\nlet u =')
pprint(u)
print('\nlet v\' =')
pprint(v_)

u_ = diff(u, x)
v = integrate(v_, x)
print('\nlet u\' =')
pprint(u_)
print('\nlet v =')
pprint(v)

part1 = u * v
part2 = u_ * v
print('\ninteg(u*v\') = u * v - integ (u\'*v)')
print('integ(u*v\') =', part1, '- integ (', part2, ')')
print('integ(u*v\') =')
f_i = part1 - integrate(part2, x)
pprint(simplify(f_i))
print('=')

# simple from here on
res = f_i.subs(x, hi) - f_i.subs(x, lo)
pprint(factor(res))
print('\n~=', res.evalf(20))
