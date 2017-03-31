def draw_line(screen, width, x1, x2, y):
    i1 = get_index(width, x1, y)
    i2 = get_index(width, x2, y)

    e1 = x1 % 8
    e2 = x2 % 8
    mask1 = 0xff >> e1
    mask2 = ~(0xff >> (e2 + 1))

    if i1 == i2:
        screen[i1] |= mask1 & mask2
    else:
        screen[i1] |= mask1
        screen[i2] |= mask2
        for i in range(i1 + 1, i2):
            screen[i] |= 0xff


def get_index(width, x, y):
    return (y * width + x) / 8
