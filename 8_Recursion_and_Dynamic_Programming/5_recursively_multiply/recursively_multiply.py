def recursively_multiply_helper(s, b):
    if s == 0:
        return 0

    if s == 1:
        return b

    temp = recursively_multiply_helper(s / 2, b)
    return temp + temp + b if s % 2 == 1 else temp + temp

def recursively_multiply(m, n):
    return recursively_multiply_helper(min(m, n), max(m, n))

assert(recursively_multiply(7, 8) == 56)
assert(recursively_multiply(7, 19) == 133)
assert(recursively_multiply(25, 32) == 800)
