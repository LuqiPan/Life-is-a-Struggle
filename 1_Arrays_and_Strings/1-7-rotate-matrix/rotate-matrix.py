def generate_matrix(n):
    return [[x * n + y for y in range(n)] for x in range(n)]

def rotate(matrix):
    dimension = len(matrix)
    for layer in range((dimension + 1) / 2):
        for j in range(layer, dimension - layer - 1):
            temp = matrix[layer][j]
            matrix[layer][j] = matrix[dimension - layer - 1 - j + layer][layer]
            matrix[dimension - layer - 1 - j + layer][layer] = matrix[dimension - layer - 1][dimension - layer - 1 - j + layer]
            matrix[dimension - layer - 1][dimension - layer - 1 - j + layer] = matrix[j][dimension - layer - 1]
            matrix[j][dimension - layer - 1] = temp

    return matrix

def helper(n):
    for array in generate_matrix(n):
        print ' '.join(['%2d' % i for i in array])

    print '-----'

    for array in rotate(
        generate_matrix(n)
    ):
        print ' '.join(['%2d' % i for i in array])

helper(5)
print '====='
helper(6)
print '====='
helper(1)
print '====='
helper(2)
