# a is the longer array
def sorted_merge(a, b, m, n):
    cur = m + n - 1
    i = m - 1
    j = n - 1
    while j >= 0:
        if a[i] > b[j]:
            a[cur] = a[i]
            i -= 1
        else:
            a[cur] = b[j]
            j -= 1

        cur -= 1

a = [1,2,5,6,0,0]
b = [3,4]
sorted_merge(a, b, 4, 2)
print a
