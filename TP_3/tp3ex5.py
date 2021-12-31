from time import time


# 1)

def harmonique(n):
    if n < 0:
        print("that's not even a thing!'")
        return -1
    if n == 0:
        return 0.0
    return harmonique(n - 1) + (1 / n)


print('rec: u(100) =', harmonique(100))
print('rec: u(950) =', harmonique(950))


# print('rec: u(1010) =', harmonique(1010)) #recursion depth > 1000 (~max)

def harmonique_imp(n):
    if n < 0:
        print("that's not even a thing!'")
        return -1
    if n == 0:
        return 0.0

    res = 0.0
    for i in range(1, n + 1):
        res += (1 / i)
    return res


print('imp: u(100) =', harmonique_imp(100))
print('imp: u(950) =', harmonique_imp(950))
print('imp: u(1010) =', harmonique_imp(1010))


# 2)


def fibo_r(n):
    if n < 0:
        print('central, we\'ve got a code brown')
        return

    if n <= 1:
        return n
    return fibo_r(n - 1) + fibo_r(n - 2)


dur_prev = 0
lo = 25
hi = 36
n = hi - lo
avg = 0
for i in range(lo, hi):
    t_start = time()
    fibo_r(i)
    t_fin = time()
    dur = t_fin - t_start
    print('exe time, fibo_r(', i, ') =', dur, 'sec')
    if not dur_prev == 0:
        avg += dur / dur_prev
        print('exe took', dur - dur_prev, 'sec more to execute')
        print('\nratio of', round(dur / dur_prev, 2), 'between exe time for two consecutive values of n\n')
    dur_prev = dur
print('avg ratio of increase in exe time:', avg / n)

# we notice that if fibo_r(n) takes t time to execute, fibo_r(n + 1) will take 1.5~1.7*t time to execute
# ... when n ≥ 30
# WHICH LOOKS A LOT LIKE THE GOLDEN RATIO OHMMMMAGGGGAAAAHD
# seems like t = t_prev + t_prev_prev, then

t_start = time()
fibo_r(30)
t_fin = time()
dur = t_fin - t_start
print('exe time, fibo_r(', 30, ') =', dur, 'sec')

# dur(fibo_r(30)) = dur(0) * 1.61803398875^30 = 0.3593761920928955 sec
# dur(fibo_r(80)) = dur(30) * 1.61803398875^50 = 320.5 years
# dur(fibo_r(120)) = dur(30) * 1.61803398875^90 = 73.3 billion years
# Yo...
