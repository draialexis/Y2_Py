#1)

def syracuse(n):
    if n < 1:
        print('nope')
        return
    i = 1
#(!)the length of the series, not the number of steps
    #print('n =', n, '->')
    while not n == 1:
        if n % 2 == 0:
            n = int(n / 2)
        else:
            n = int(((n * 3) + 1) / 2)
#division by 2 is a shortcut, not how the pb usually appears online
        #print('n =', n, '->')
        i += 1
    return i

print('syracuse( -1 ) =', syracuse(-1))
print('syracuse( 0 ) =', syracuse(0))
print('syracuse( 10 ) =', syracuse(10))
print('syracuse( 100 ) =', syracuse(100))

#2)

for n in range(10, 26):
    print('syracuse(', n ,') =', syracuse(n))

#3) + 4)

lmax = 0
nmax = 0
for n in range(10, 10000):
    x = syracuse(n)
    if x > lmax:
        lmax = x
        nmax = n

print('lmax syracuse in [10-10_000] =', lmax)
print('nmax syracuse in [10-10_000] =', nmax)

#nmax = 6171, lmax = 166
#https://en.wikipedia.org/wiki/Collatz_conjecture