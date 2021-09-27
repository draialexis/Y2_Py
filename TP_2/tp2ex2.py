import math as m

#2)

a = 3

v = m.log((1 + a) / a)
print('v1 =', v)
prev = v
n = 2 #(!) n >= 2

while(not n > 40):
    v = (1 / (n - 1)) - (a * prev)
    prev = v
    print('at n =', n ,', v =', v)

    n += 1

    #this gets wild... v -> 0 when n -> + inf, but rounding error seems to
    #make v spike back up at around n = 30
    #v40 = 253.080... somehow

print('yaouch')

#3)

v = ((1 / 180) + (1 / 240)) / 2
print('v60 =', v)
prev = v
n = 60

while(not n < 40):
    v = - (prev - (1 / (n - 1)) / a)
    prev = v
    print('at n =', n ,', v =', v)

    n -= 1

print('that\'s better')