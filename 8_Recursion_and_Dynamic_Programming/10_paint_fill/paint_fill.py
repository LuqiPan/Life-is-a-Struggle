def paint_fill(matrix, x, y, old, new):
    if x >= len(matrix) or x < 0:
        return

    if y >= len(matrix[0]) or y < 0:
        return

    if matrix[x][y] != old:
        return

    if matrix[x][y] == new:
        return

    matrix[x][y] = new
    paint_fill(matrix, x - 1, y, old, new)
    paint_fill(matrix, x + 1, y, old, new)
    paint_fill(matrix, x, y - 1, old, new)
    paint_fill(matrix, x, y + 1, old, new)
