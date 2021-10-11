# 1)

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


# str = "CESAR"
# for lt in str:
#    print(code_une(lt))
# print('\n')


# 2)

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


# my_code = [2, 4, 18, 0, 17]
# for c in my_code:
#     print(decode_une(c))
# print('\n')


# 3)

def encode(str_p):
    res = map(code_une, str_p)
    return res


# my_word = 'PYTHON'


def decode(code):
    char_list = map(decode_une, code)
    res = "".join(char_list)
    return res

# my_code = code_mot(my_word)
# print(my_word, '\n->')
# print(code_mot(my_word), '\n->')
# print(decode_mot(my_code), '\n')
