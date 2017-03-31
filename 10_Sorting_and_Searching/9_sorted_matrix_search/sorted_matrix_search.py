def sorted_matrix_search(matrix, i_start, j_start, i_end, j_end, target):
    if i_start > i_end or j_start > j_end:
        return None

    i_mid = (i_start + i_end) / 2
    j_mid = (j_start + j_end) / 2

    if matrix[i_mid][j_mid] == target:
        return (i_mid, j_mid)

    if matrix[i_mid][j_mid] > target:
        #Eliminate bottom right
        ######
        ######
        ######
        ###---
        ###---
        ###---
        return
            #top left
            sorted_matrix_search(matrix, i_start, j_start, i_mid - 1, j_mid - 1, target)
            #bottom left
            or sorted_matrix_search(matrix, i_mid, j_start, i_end, j_mid - 1, target)
            #top right
            or sorted_matrix_search(matrix, i_start, j_mid, i_mid - 1, j_end, target)
    else:
        #Eliminate top left
        return
            #bottom right
            sorted_matrix_search(matrix, i_mid + 1, j_mid + 1, i_end, j_end, target)
            #bottom left
            or sorted_matrix_search(matrix, i_mid + 1, j_start, i_end, j_mid, target)
            #top right
            or sorted_matrix_search(matrix, i_start, j_mid + 1, i_mid, j_end, target)
