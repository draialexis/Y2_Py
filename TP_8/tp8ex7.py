import numpy as np
print('\n=============1)=============\n')

def dicho(f, a, b, eps):
    if a == b: #interval can't be nothing
        print("[", a, ",", b, "] is not a thing...")
        return None
    if a > b: #interval shouldn't be [b, a]
        tmp = a
        a = b
        b = tmp

    m = (a + b) / 2
    c = 0
    while abs(f(m)) > eps:
        c += 1
        print("\nc:", c)
        print("[a, b] = [", a, ",", b, "]")
        print("m = (a + b) / 2 = ", m)
        print("abs(f(m))=", abs(f(m)))
        if f(a) * f(m) < 0: #sign changed between a and m
            b = m #new upper bound is m: midpoint
        elif f(b) * f(m) < 0:
            a = m
        else:
            print("sign doesn't change in [", a, ",", b, "]...")
            return None

        if(c > 100): #arbitrary, could be dynamic or chosen by input
            print("can't find it...")
            return None
        m = (a + b) / 2

    print("\n\n[a, b] = [", a, ",", b, "]")
    print("abs(f(m))=", abs(f(m)))
    return m

epsilon =  pow(10, -8)
f = lambda x: np.sin(x) - np.log(x)
print(dicho(f, 0.1, 4, epsilon)) #putting b around pi seems like it'll work

print('\n=============2)=============\n')

f = lambda x: 2*x + 3 - pow(np.e, x)
#appropriate intervals are [-2, 0] and [0, 2]
print("x | f(x) = 0 =\n", dicho(f, -2, 0, epsilon))
print("x | f(x) = 0 =\n", dicho(f, 1, 1400, epsilon))

"""
number of iterations depends on the intervals we chose.
if we were looking for a solution for sin(x) = 0, and if we chose [pi/2, 3pi/2],
then we'd only need 1 iteration ((pi/2 + 3pi/2) / 2 = pi, and sin(pi)=0)

so how do we know which intervals to chose ?

ps: we use divide and rule here... I think that means we're looking at O(n*log(n))
: even with a huge interval, since we're dividing it by 2 at every iteration,
it shrinks pretty fast...
"""
