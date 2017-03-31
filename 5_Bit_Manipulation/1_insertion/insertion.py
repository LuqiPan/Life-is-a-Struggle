def insert(n, m, i, j):
    assert i < j
    high_mask = ~1 << (j + 1)
    low_mask = 1 << i - 1
    mask = high_mask | low_mask
    return n & mask | (m << i)

print bin(insert(int('10000000000', 2), int('10011', 2), 2, 6))
