from copy import deepcopy

def permutation_without_dups(chars):
    if len(chars) == 1:
        return [[chars[0]]]

    sub = permutation_without_dups(deepcopy(chars[:-1]))
    result = []
    for perm in sub:
        for i in range(len(sub) + 1):
            new_perm = deepcopy(perm)
            new_perm.insert(i, chars[-1])
            result.append(new_perm)

    return result

print permutation_without_dups([1])
print permutation_without_dups([1, 2])
print permutation_without_dups([1, 2, 3])
