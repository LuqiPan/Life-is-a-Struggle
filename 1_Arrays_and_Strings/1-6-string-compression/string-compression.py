def compress(string):
    current_char = string[0]
    count = 0
    result = ''
    for c in string:
        if c == current_char:
            count = count + 1
        else:
            result = result + current_char
            result = result + str(count + 1)
            current_char = c
            count = 0

    result = result + current_char
    result = result + str(count + 1)

    if len(result) < len(string):
        return result
    else:
        return string

print compress('abcdefg')
print '-----'
print compress('aabcccccaaa')
print compress('aabccccca')
print compress('aabccccc')
