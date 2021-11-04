def code_une(lt):
    switcher = {
        'A': 0,
        'B': 1,
        'C': 2,
        'D': 3,
        'E': 4,
        'F': 5,
        'G': 6,
        'H': 7,
        'I': 8,
        'J': 9,
        'K': 10,
        'L': 11,
        'M': 12,
        'N': 13,
        'O': 14,
        'P': 15,
        'Q': 16,
        'R': 17,
        'S': 18,
        'T': 19,
        'U': 20,
        'V': 21,
        'W': 22,
        'X': 23,
        'Y': 24,
        'Z': 25,
        ' ': ' ',
    }
    return switcher.get(lt, '#')


def decode_une(c):
    switcher = {
        0: 'A',
        1: 'B',
        2: 'C',
        3: 'D',
        4: 'E',
        5: 'F',
        6: 'G',
        7: 'H',
        8: 'I',
        9: 'J',
        10: 'K',
        11: 'L',
        12: 'M',
        13: 'N',
        14: 'O',
        15: 'P',
        16: 'Q',
        17: 'R',
        18: 'S',
        19: 'T',
        20: 'U',
        21: 'V',
        22: 'W',
        23: 'X',
        24: 'Y',
        25: 'Z',
        ' ': ' ',
    }
    return switcher.get(c, '#')


def encode(str_p):
    res = list(map(code_une, str_p))
    return res


def decode(code):
    char_list = list(map(decode_une, code))
    res = "".join(char_list)
    return res


# 1)
# 2)

def cesar(string, d, is_decypher):
    if is_decypher:
        d = -1 * d
    nums = encode(string)
    nums_delta = []
    for num in nums:
        if isinstance(num, int):
            nums_delta.append((num + d) % 26)
        elif num == ' ':
            nums_delta.append(num)

    res = decode(nums_delta)
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
for i in range(1, 26):
    candidate = cesar(test, i, 1)
    result = candidate.find('THE')
    if result == 0:
        print('i =', i, '|', candidate)

# i = 17 | THE ART OF PROGRAMMING IS THE ART OF ORGANIZING COMPLEXITY
# (E. W. Dijkstra)
