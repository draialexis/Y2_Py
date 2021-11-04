import sympy as sm

sm.var('a b c x h u v w')

# 1)

p = a * x ** 2 + b * x + c

exp1 = p.subs(x, 0) - u
exp2 = p.subs(x, h / 2) - v
exp3 = p.subs(x, h) - w
s = sm.solve([exp1, exp2, exp3], [a, b, c])
sm.pprint(s)

# 2)

p = p.subs(s)
sm.pprint(p)

# 3)

s = {
    u: 0,
    v: 2,
    w: 1,
    h: 2
}

exp1 = exp1.subs(s)
exp2 = exp2.subs(s)
exp3 = exp3.subs(s)
p = p.subs(s)
s = sm.solve([exp1, exp2, exp3], [a, b, c])
sm.pprint(s)

p = p.subs(s)
sm.pprint(p)

sm.plot(p, (x, 0, 2))
