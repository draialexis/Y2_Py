import tp3ex1 as prv

def gcd(a, b):
    while b != 0:
        r = a % b
        a = b
        b = r
    return a


# 1)

# "Supposons que 'a' est premier avec 26" -> p(a, 26) = 1
for i in range(26):
    res = gcd(i, 26)
    if res == 1:
        print(i, 'is coprime with 26')


# 2)
# au lieu d'appliquer un decalage d a chaque lettre
# codee f(n) = n+d % 26 (n € [0; 25]),
# on applique une fonction affine
# f(n) = an+b % 26
# (pour une valeur admissible de a).

def affine(string, a, b):
    nums = prv.encode(string)
    nums_delta = []
    for num in nums:
        if isinstance(num, int):
            # print('num:', num)
            # print('alpha:', (a * num + b))
            # print('alpha modulo 26:', (a * num + b) % 26)
            nums_delta.append((a * num + b) % 26)
        elif num == ' ':
            nums_delta.append(num)

    return prv.decode(nums_delta)


my_string = 'CONFIDENTIEL'
my_a = 5
my_b = 7
my_enc_string = affine(my_string, my_a, my_b)
print('str:', my_string)
print('enc_str:', my_enc_string)

# 3)

cst = 26


def inverse(a):
    for i in range(1, cst):
        a_m = a % cst
        i_m = i % cst
        a_i_m = a_m * i_m % cst
        if a_i_m == 1:
            return i
    return 0


# for x in range(1, cst+1):
#    inv = inverse(x)
#    if inv == 0:
#        print('cannot find an "inverse modulo 26" for', x)
#    else:
#        print(x, '*', inv, '%', cst, '=', 1)


# 4)

def de_affine(string, a, b):
    nums = prv.encode(string)
    nums_delta = []
    for num in nums:
        if isinstance(num, int):
            # print('num:', num)
            # print('num-b:', num-b)
            # print('(num-b)*inverse(a):', (num-b)*inverse(a))
            # print('((num-b)*inverse(a))%26:', ((num-b)*inverse(a))%26)

            nums_delta.append(((num - b) * inverse(a)) % 26)
        elif num == ' ':
            nums_delta.append(num)

    return prv.decode(nums_delta)


my_dec_string = de_affine(my_enc_string, my_a, my_b)

print('dec_str:', my_dec_string)

for i in [1, 3, 5, 7, 9]:  # we choose these 'a's in [1, 9[ because even numbers don't have an inverse mod 26
    for j in range(1, 10):
        print('dec_kybix (i=', i, 'j=', j, '):', de_affine('KYBIX', i, j))
# dec_kybix (i= 9 j= 1 ): BRAVO

for i in range(1, 27):
    print('b=', i, ':', de_affine('LP NVP UJVR YCJAVXRJUR L PRG AP QH LJFYCPIPURXJU', 15, i))
# b= 7 : CE QUE NOUS PRODUISONS C EST DE LA COMPREHENSION
