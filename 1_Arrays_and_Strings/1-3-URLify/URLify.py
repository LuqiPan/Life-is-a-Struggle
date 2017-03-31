def URLify(input, length):
    curr = len(input) - 1
    for i in range(length - 1, -1, -1):
        if input[i] == ' ':
            input[curr] = '0'
            input[curr-1] = '2'
            input[curr-2] = '%'
            curr = curr - 3
        else:
            input[curr] = input[i]
            curr = curr - 1

    return input

input = list('Mr John Smith    ')
print ''.join(URLify(input, 13))
