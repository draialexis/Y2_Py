def pgcd(a, b):
    while b != 0:
        r = a % b
        # print(a, '%', b, '=', r)
        a = b
        b = r
    return a


# print('pgcd (495, 275) =', pgcd(495, 275))
# print('pgcd (495, 275) =', pgcd(200, 80))
