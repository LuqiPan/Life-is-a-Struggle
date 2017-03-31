# this function only works on positive numbers since python only has arithmetical
# right shift operator
def flip_bit_to_win(number):
    current_length = 0
    previous_length = 0
    max_length = 0
    while number != 0:
        if (number & 1) == 1:
            current_length += 1
        else:
            previous_length = 0 if (number & 2) == 0 else current_length
            current_length = 0

        number >>= 1
        max_length = max(max_length, current_length + previous_length + 1)

    return max_length

print flip_bit_to_win(1775)
