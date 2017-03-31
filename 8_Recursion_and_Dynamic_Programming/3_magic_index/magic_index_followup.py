def magic_index_helper(array, left, right):
    if (left > right) or left >= len(array) or right < 0:
        return None

    mid = (left + right) / 2
    if array[mid] == mid:
        return mid

    # 1 2 3 4 4 6
    # 0 1 2 3 4 5
    if array[mid] > mid:
        return magic_index_helper(array, left, mid - 1) or magic_index_helper(array, array[mid], right)

    return magic_index_helper(array, mid + 1, right) or magic_index_helper(array, left, array[mid])

def magic_index(array):
    return magic_index_helper(array, 0, len(array) - 1)

assert(magic_index([-10, -5, 2, 2, 2, 3, 4, 7, 9, 12, 13]) == 7)
