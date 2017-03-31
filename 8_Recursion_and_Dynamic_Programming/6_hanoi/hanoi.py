# N 0 0
# a b c

def hanoi(n, from_tower, to_tower, intermediate_tower):
    if n == 1:
        print "{} -> {}".format(from_tower, to_tower)
        return

    hanoi(n - 1, from_tower, intermediate_tower, to_tower)
    print "{} -> {}".format(from_tower, to_tower)
    hanoi(n - 1, intermediate_tower, to_tower, from_tower)

def hanoi_helper(n):
    hanoi(n, 'a', 'b', 'c')

hanoi_helper(1)
print '-----'
hanoi_helper(2)
print '-----'
hanoi_helper(3)
