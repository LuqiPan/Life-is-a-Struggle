def rotate(matrix, x, dimension):
    if dimension <= 1:
        return matrix

    for distance in range(0, dimension - 1):
        temp = matrix[x][x + distance]
        matrix[x][x + distance] = matrix[x + dimension - 1 - distance][x]
        matrix[x + dimension - 1 - distance][x] = matrix[x + dimension - 1][x + dimension - 1 - distance]
        matrix[x + dimension - 1][x + dimension - 1 - distance] = matrix[x + distance][x + dimension - 1]
        matrix[x + distance][x + dimension - 1] = temp

    return rotate(matrix, x + 1, dimension - 2)

def generate_matrix(n):
    return [[x * n + y for y in range(n)] for x in range(n)]

def helper(n):
    for array in generate_matrix(n):
        print ' '.join(['%2d' % i for i in array])

    print '-----'

    for array in rotate(
        generate_matrix(n),
        0,
        n
    ):
        print ' '.join(['%2d' % i for i in array])

helper(5)
print '====='
helper(6)
print '====='
helper(1)
print '====='
helper(2)
