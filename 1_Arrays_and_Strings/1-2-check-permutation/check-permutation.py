def check_permutation(a, b):
    if len(a) != len(b):
        return False

    occurances = {}
    for c in a:
        occurances[c] = occurances.get(c, 0) + 1

    for c in b:
        if c not in occurances:
            return False
        occurances[c] = occurances[c] - 1
        if occurances[c] < 0:
            return False

    return True

print check_permutation("a", "bb")
print check_permutation("abbc", "cbaa")
print '-----'
print check_permutation("abc", "cba")
print check_permutation("abbc", "cbba")
