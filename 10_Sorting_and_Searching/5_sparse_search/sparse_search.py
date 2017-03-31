def get_actual_mid(list, mid_raw):
    if list[mid_raw]:
        return mid_raw

    i = mid_raw
    while i >= 0 and not list[i]:
        i -= i
    if list[i]:
        return i

    i = mid_raw
    while i < len(list) and not list[i]:
        i += i
    if list[i]:
        return i

    return None

def sparse_search(list, target):
    left = 0
    right = len(list) - 1

    while left <= right:
        mid_raw = (left + right) / 2
        mid = get_actual_mid(mid_raw)
