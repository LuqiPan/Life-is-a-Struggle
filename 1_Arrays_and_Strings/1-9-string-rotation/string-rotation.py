def is_rotation(a_string, another_string):
    if len(a_string) != len(another_string):
        return False

    a_string = a_string + a_string
    return another_string in a_string

print is_rotation('waterbottle', 'erbottlewat')
print is_rotation('erbottlewat', 'waterbottle')
print is_rotation('abc', 'cab')
print is_rotation('cab', 'abc')
print is_rotation('abc', 'bca')
print is_rotation('bca', 'abc')
print is_rotation('cab', 'bca')
print is_rotation('bca', 'cab')
print '-----'
print is_rotation('abc', 'ab')
print is_rotation('abc', 'cba')
