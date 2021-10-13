from time import time


# 1)

def harmonique(n):
    if n < 0:
        print("that's not even a thing!'")
        return -1
    if n == 0:
        return 0.0
    return (harmonique(n - 1) + (1 / n))

print('u(100) =', harmonique(100))
print('u(950) =', harmonique(950))
#print('u(1010) =', harmonique(1010)) #recursion depth > 1000 (~max)

# this doesn't work and I don't know why
#
#def harmonique_imp(n):
#    if n < 0:
#        print("that's not even a thing!'")
#        return -1
#    if n == 0:
#        return 0.0
#
#    res = 0.0
#    prev = 0.0
#    tmp = 0.0
#    for i in range (1, n + 1):
#        tmp = res
#        res = prev + (1 / n)
#        print('i =', i, '| res =', res)
#        prev = res
#    return res
#
#print('u(100) =', harmonique_imp(100))
#print('u(950) =', harmonique_imp(950))
#print('u(1010) =', harmonique_imp(1010))

# 2)


def fibo_r(n):
    if n < 0:
        print('central, we\'ve got a code brown')
        return

    if n <= 1:
        return n
    return (fibo_r(n - 1) + fibo_r(n - 2))

dur_prev = 0
for i in range(25, 36):
    t_start= time()
    fibo_r(i)
    t_fin = time()
    dur = t_fin - t_start
    print('exe time, fibo_r(',i,') =', dur, 'sec')
    if dur_prev == 0:
        print('exe took', dur, 'sec')
    else:
        print('exe took', dur - dur_prev, 'sec more to execute')
        print('\nratio of', (((dur / dur_prev)*100)//1)/100, 'between two consecutive values of n\n')
    dur_prev = dur

# we notice that if fibo_r(n) takes 1*t time to execute, fibo_r(n + 1) will take 1.5~1.7*t time to execute
# WHICH LOOKS A LOT LIKE THE GOLDEN RATIO OHMMMMAGGGGAAAAHD
# seems like t = t_prev + t_prec_prev

# 3)

# 0.6 (t(0))

# dur(fibo_r(80)) = 0.6 * 1.61803398875^80 = 3.1416838e+16 sec
# dur(fibo_r(120)) = 0.6 * 1.61803398875^120 = 7.1889933e+24 sec
# Yo...