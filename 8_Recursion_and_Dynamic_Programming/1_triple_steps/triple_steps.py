def triple_steps(n):
    if n == 1:
        return 1

    if n == 2:
        return 2

    if n == 3:
        return 4

    a = 1
    b = 2
    c = 4
    for i in range(4, n + 1):
        d = a + b + c
        a = b
        b = c
        c = d

    return d

assert(triple_steps(4) == 7)
assert(triple_steps(5) == 13)
