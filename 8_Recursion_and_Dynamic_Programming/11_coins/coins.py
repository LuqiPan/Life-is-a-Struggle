def coins(n):
    memo = [0, 1]
    for i in range(2, n + 1):
        memo.append(memo[i - 1])
        if i - 5 >= 0:
            memo[i] += memo[i - 5]
        if i - 25 >= 0:
            memo[i] += memo[i - 25]

    return memo[n]

for i in range(27):
    print '{}: {}'.format(i, coins(i))
