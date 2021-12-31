"""
DIX² + UN² = CENTUN
"""
for d in range(1, 10):
    for i in range(0, 10):
        if i != d:
            for x in range(0, 10):
                if x != d and x != i:
                    for u in range(1, 10):
                        if u != d and u != i and u != x:
                            for n in range(0, 10):
                                if n != d and n != i and n != x and n != u:
                                    for c in range(1, 10):
                                        if c != d and c != i and c != x and c != u and c != n:
                                            for e in range(0, 10):
                                                if e != d and e != i and e != x and e != u and e != n and e != c:
                                                    for t in range(0, 10):
                                                        if t != d and t != i and t != x and t != u and t != n and t != c and t != e:
                                                            dix = (d * 100) + (i * 10) + x
                                                            un = (u * 10) + n
                                                            centun = (c * 100000) + (e * 10000) + (n * 1000) + \
                                                                     (t * 100) + (u * 10) + n
                                                            if pow(dix, 2) + pow(un, 2) == centun:
                                                                print('DIX =', dix)
                                                                print('UN =', un)
                                                                print('CENTUN =', centun)

"""
DIX = 480
UN = 76
CENTUN = 236176
"""
