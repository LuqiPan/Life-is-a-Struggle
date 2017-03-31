def zero_matrix(matrix):
    m = len(matrix)
    n = len(matrix[0])

    row = False
    col = False
    for j in range(n):
        if matrix[0][j] == 0:
            row = True

    for i in range(m):
        if matrix[i][0] == 0:
            col = True

    for i in range(1, m):
        for j in range(1, n):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0

    for i in range(1, m):
        for j in range(1, n):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0

    if row:
        for j in range(0, n):
            matrix[0][j] = 0

    if col:
        for i in range(0, m):
            matrix[i][0] = 0

    return matrix

def print_matrix(matrix):
    for row in matrix:
        print ' '.join([str(i) for i in row])

test1 = [
    [1,2,3],
    [1,0,1],
    [1,1,1]
]
print_matrix(test1)
print '-----'
print_matrix(zero_matrix(test1))
print '====='

test2 = [
    [0,1,0],
    [1,1,1],
    [1,1,1]
]
print_matrix(test2)
print '-----'
print_matrix(zero_matrix(test2))
print '====='

test3 = [
    [0,1,1],
    [1,1,1],
    [1,1,1]
]
print_matrix(test3)
print '-----'
print_matrix(zero_matrix(test3))
print '====='

test4 = [
    [1,1,0],
    [1,1,1],
    [1,1,1]
]
print_matrix(test4)
print '-----'
print_matrix(zero_matrix(test4))
print '====='
