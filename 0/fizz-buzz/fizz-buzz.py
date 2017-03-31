def fizzBuzz(n):
    """
    :type n: int
    :rtype: List[str]
    """
    result = []
    for i in range(1, n + 1):
        current_str = ''
        if i % 3 == 0:
            current_str += 'Fizz'

        if i % 5 == 0:
            current_str += 'Buzz'

        if current_str == '':
            current_str = str(i)

        result.append(current_str)

    return result

print fizzBuzz(15)
