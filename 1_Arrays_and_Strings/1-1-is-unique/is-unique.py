alphabet = set(list('abcdefg'))

def is_unique(str):
    if len(str) != len(alphabet):
        return False

    seen_chars = set()
    for c in list(str):
        if c not in seen_chars:
            seen_chars.add(c)
        else:
            return False

    return True

print is_unique('abcdefg')
print is_unique('cdeabfg')
print '-----'
print is_unique('abcdef')
print is_unique('abcdeff')
