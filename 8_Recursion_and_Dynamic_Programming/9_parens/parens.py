from copy import deepcopy

def parens(n):
    result = []
    parens_helper(n, n, '', result)
    print result

def parens_helper(left, right, current_seq, result):
    if left == 0 and right == 0:
        result.append(current_seq)
        return

    if left > 0:
        new_seq = deepcopy(current_seq)
        new_seq += '('
        parens_helper(left - 1, right, new_seq, result)

    if right > 0 and right > left:
        new_seq = deepcopy(current_seq)
        new_seq += ')'
        parens_helper(left, right - 1, new_seq, result)

parens(3)
