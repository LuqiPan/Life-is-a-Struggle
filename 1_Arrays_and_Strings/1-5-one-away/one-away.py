def one_away(a, b):
    if abs(len(a) - len(b)) > 1:
        return False

    i = 0
    j = 0
    count = 0

    while i < len(a) - 1 and j < len(b) - 1:
        if a[i] == b[j]:
            i = i + 1
            j = j + 1
        else:
            count = count + 1
            if count > 1:
                return False
            if a[i + 1] == b[j + 1]:
                i = i + 1
                j = j + 1
            elif a[i + 1] == b[j]:
                i = i + 1
            elif a[i] == b[j + 1]:
                j = j + 1
            else:
                return False

    if i == len(a) - 1 and j == len(b) - 1:
        if a[i] == b[j]:
            return True
        else:
            count = count + 1
    elif i != len(a) - 1:
        if a[i] == b[j]:
            count = count + 1
        else:
            if a[i+1] == b[j]:
                count = count + 1
            else:
                return False
    else:
        if a[i] == b[j]:
            count = count + 1
        else:
            if b[j+1] == a[i]:
                count = count + 1
            else:
                return False

    return count <= 1

print one_away('pale', 'ple')
print one_away('ple', 'pale')
print one_away('pale', 'pala')
print one_away('pales', 'pale')
print one_away('pale', 'pales')
print one_away('pale', 'bale')
print '-----'
print one_away('pale', 'bake')
print one_away('pale', 'poke')
print one_away('pale', 'bales')
print one_away('pales', 'bale')
print one_away('pales', 'baled')
