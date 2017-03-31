def power_set(set):
    return [pick(set, i) for i in range(2 ** len(set))]

def pick(set, n):
    result = []
    index = 0
    while n != 0:
        if n & 1:
            result.append(set[index])

        n = n >> 1
        index += 1

    return result

print power_set([1])
print power_set([1, 2])
print power_set([1, 2, 3])
