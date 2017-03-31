def magic_index(array, left, right):
    if (left > right):
        return None

    mid = (left + right) / 2
    if array[mid] == mid:
        return mid

    # 0, 2, 4
    if array[mid] > mid:
        return magic_index(array, left, mid - 1)

    return magic_index(array, mid + 1, right)

def magic_index_helper(array):
    return magic_index(array, 0, len(array) - 1)

assert(magic_index_helper([0, 2, 4]) == 0)
assert(magic_index_helper([-1, 0, 2]) == 2)
assert(magic_index_helper([-1, 1, 3]) == 1)
