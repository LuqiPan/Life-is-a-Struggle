def search_in_rotated_array(array, left, right, target):
    if (left > right):
        return None

    mid = (left + right) / 2
    if array[mid] == target:
        return mid

    if array[left] < array[mid]:
        if array[left] <= target and target < array[mid]:
            return search_in_rotated_array(array, left, mid - 1, target)
        else:
            return search_in_rotated_array(array, mid + 1, right, target)
    elif array[mid] < array[right]:
        if array[mid] < target and target <= array[right]:
            return search_in_rotated_array(array, mid + 1, right, target)
        else:
            return search_in_rotated_array(array, left, mid - 1, target)
    elif array[left] == array[mid]:
        if array[right] != array[mid]:
            return search_in_rotated_array(array, mid + 1, right, target)
        else:
            return search_in_rotated_array(array, left, mid - 1, target) or search_in_rotated_array(array, mid + 1, right, target)

    return None
