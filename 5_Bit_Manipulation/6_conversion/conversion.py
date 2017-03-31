def conversion(a, b):
    n = a ^ b
    count = 0
    while n != 0:
        if n & 1 == 1:
            count += 1

        n = n / 2

    return count

print conversion(29, 15)
print conversion(15, 29)
