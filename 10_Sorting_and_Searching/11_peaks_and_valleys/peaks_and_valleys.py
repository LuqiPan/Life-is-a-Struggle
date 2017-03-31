import sys

def peaks_and_valleys(array):
    for i in range(1, len(array), 2):
        max_index = biggest_index(array, i - 1, i, i + 1)
        if max_index != i:
            temp = array[i]
            array[i] = array[max_index]
            array[max_index] = temp

def biggest_index(array, a, b, c):
    a_value = array[a] if a >= 0 and a < len(array) else -sys.maxint
    b_value = array[b] if b >= 0 and b < len(array) else -sys.maxint
    c_value = array[c] if c >= 0 and c < len(array) else -sys.maxint

    max_value = max(a_value, b_value, c_value)
    if max_value == a_value:
        return a
    if max_value == b_value:
        return b
    if max_value == c_value:
        return c

array = [0,1,4,7,8,9]
peaks_and_valleys(array)
print array
