def generate_matrix(n):
    return [[x * n + y + 1 for y in range(n)] for x in range(n)]

def spiral_print(matrix, x, y, m, n):
    if m == 0 or n == 0:
        return

    if m == 1 and n == 1:
        print matrix[x][y]
        return

    if m == 1:
        for j in range(y, y + n):
            print matrix[x][j]
        return

    if n == 1:
        for i in range(x, x + m):
            print matrix[i][y]
        return

    for j in range(y, y + n):
        print matrix[x][j]

    for i in range(x + 1, x + m):
        print matrix[i][y + n - 1]

    for j in range(y + n - 2, x - 1, -1):
        print matrix[x + m - 1][j]

    for i in range(x + m - 2, x, -1):
        print matrix[i][y]

    spiral_print(matrix, x + 1, y + 1, m - 2, n - 2)

def helper(n):
    spiral_print(generate_matrix(n), 0, 0, n, n)

helper(1)
print '------'
helper(2)
print '------'
helper(3)
print '------'
helper(4)
print '------'

def generate_2d_array(m, n):
    return [[i * n + j + 1 for j in range(n)] for i in range(m)]

def array_helper(m, n):
    print generate_2d_array(m, n)
    spiral_print(generate_2d_array(m, n), 0, 0, m, n)

array_helper(3, 6)
