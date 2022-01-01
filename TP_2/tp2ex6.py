# 1)

def gcd(a, b):
    while b != 0:
        r = a % b
        a = b
        b = r
    return a


print('gcd(123456, 234567) =', gcd(123456, 234567))


# 2)

def phi(n):
    if n == 0:
        print('no no no no no')
        return -1
    count = 0
    for i in range(1, n + 1):
        if gcd(i, n) == 1:
            # print(i, '/', n)
            count += 1
    return count


print('phi(10) =', phi(10))
print('phi(30) =', phi(30))


# 3)

def farey(n):
    res = [0]
    if n == 0:
        print('no no no no no')
        return -1
    # print('0 / 1')
    for i in range(1, n + 1):
        j = n
        while j > 0:
            if gcd(i, j) == 1 and i < j:
                # print(i, '/', j)
                res.append(i / j)
            j -= 1

    # print('1 / 1')
    res.append(1)
    return res


test = farey(4)
print('farey( 4 ) =', test, '\nsize:', len(test))

for i in range(10, 31):
    test = farey(i)
    print('farey(', i, ') =', test, '\nsize:', len(test))
