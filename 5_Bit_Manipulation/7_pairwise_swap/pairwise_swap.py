def pairwise_swap(n):
    return ((n & 0xaaaaaaaaaaaaaaaa) >> 1) | ((n & 0x5555555555555555) << 1)
