alphabet = 'abcdefg'

def is_unique(str):
    if len(alphabet) != len(str):
        return False

    str = ''.join(sorted(str))
    for i in range(len(str) - 1):
        if str[i] == str[i+1]:
            return False

    return True

print is_unique('abcdefg')
print is_unique('cdeabfg')
print '-----'
print is_unique('abcdef')
print is_unique('abcdeff')
