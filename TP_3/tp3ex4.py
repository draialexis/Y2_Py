def factorial(n):
    if n == 1:
        return 1
    elif n > 1:
        return n * factorial(n - 1)
    else:
        print("Nnnno no no")


def euler(n):
    if n == 0:
        return 1
    elif n > 0:
        #        print('factorial(',n , ') =', factorial(n))
        return euler(n - 1) + 1 / (factorial(n))
    else:
        print("that's a woopsie...'")
        return


my_n = 20
print('euler(', my_n, ') =', euler(my_n))
# oh, hey, Euler's number...
