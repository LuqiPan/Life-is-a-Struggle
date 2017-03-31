def binary_to_string(number):
    if number >= 1 or number <= 0:
        return "ERROR"

    result = ''
    while (number > 0):
        if len(result) > 32:
            return "ERROR"

        number = number * 2
        if number >= 1:
            result += '1'
            number -= 1
        else:
            result += '0'

    return '0b0.' + result

print binary_to_string(0.5)
print binary_to_string(0.75)
