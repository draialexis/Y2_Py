def gcd(a, b):
    while b != 0:
        r = a % b
        a = b
        b = r
    return a


print('gcd(495, 275) =', gcd(495, 275))
print('gcd(200, 80) =', gcd(200, 80))
