def get_approximate_size(listy):
    size = 1
    while listy.element_at(size - 1) != -1:
        size *= 2

    return size - 1

def binary_search(listy, target):
    approximate_size = get_approximate_size(listy)
    left = 0
    right = approximate_size - 1

    while left <= right:
        mid = (left + right) / 2
        if listy.element_at(mid) != -1:
            if listy.element_at(mid) == target:
                return mid
            elif listy.element_at(mid) > target:
                right = mid - 1
            else:
                left = mid + 1
        else:
            right = mid -1

    return None
