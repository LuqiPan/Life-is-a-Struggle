from copy import deepcopy

def permutation_without_dups(chars, current_seq, result):
    if not chars:
        result.append(current_seq)
        return

    for c in chars:
        new_seq = deepcopy(current_seq)
        new_seq.append(c)
        new_chars = deepcopy(chars)
        new_chars.remove(c)
        permutation_without_dups(new_chars, new_seq, result)

def permutation_without_dups_helper(chars):
    result = []
    permutation_without_dups(chars, [], result)
    print result

permutation_without_dups_helper([1])
permutation_without_dups_helper([1, 2])
permutation_without_dups_helper([1, 2, 3])
