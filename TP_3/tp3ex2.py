import tp3ex1 as prv


# 1)
# 2)

def code_str(string):
    words = string.split()
    res = []
    for word in words:
        res.append(prv.code_mot(word))
    return res


def decode_str(nums):
    str_arr = []
    for num_arr in nums:
        str_arr.append(prv.decode_mot(num_arr))
    res = " ".join(str_arr)
    return res


def cypher(num, d):
    # print(num, '->', num + d)
    num += d
    if num >= 26 or num < 0:
        # print('___', num, '->', num % 26)
        num = num % 26
    return num


def cesar(string, d, is_decypher):
    if is_decypher:
        d = -1 * d
    nums = code_str(string)
    nums_delta = []
    for num_arr in nums:
        nums_delta_i = []
        for num in num_arr:
            nums_delta_i.append(cypher(num, d))
        nums_delta.append(nums_delta_i)

    res = decode_str(nums_delta)
    return res


# 3)

my_str = 'CE MESSAGE EST CONFIDENTIEL'
delta = -11
print(my_str, '| delta =', delta)

encyphered = cesar(my_str, delta, 0)
print(encyphered)
decyphered = cesar(encyphered, delta, 1)
print(decyphered)

# 4)

test = 'KYV RIK FW GIFXIRDDZEX ZJ KYV RIK FW FIXREZQZEX TFDGCVOZKP'
for i in range(1, 27):
    print('i =', i, '|', cesar(test, i, 1))
    # i = 17 | THE ART OF PROGRAMMING IS THE ART OF ORGANIZING COMPLEXITY
    # (E. W. Dijkstra)
