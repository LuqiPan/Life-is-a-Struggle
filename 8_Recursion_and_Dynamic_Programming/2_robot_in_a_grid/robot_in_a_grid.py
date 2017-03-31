def robot_in_a_grid(r, c):
    memo = []
    for i in range(r):
        memo.append([1])

    for j in range(1, c):
        memo[0].append(1)

    for row in range(1, r):
        for col in range(1, c):
            memo[row].append(memo[row - 1][col] + memo[row][col - 1])

    return memo[r - 1][c - 1]

print robot_in_a_grid(1,5)
print robot_in_a_grid(5,1)
print robot_in_a_grid(2,5)
print robot_in_a_grid(5,5)
