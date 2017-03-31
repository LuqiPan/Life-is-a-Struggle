from collections import defaultdict
from copy import deepcopy

def permutation_with_dups(chars):
    key_count = defaultdict(int)
    for c in chars:
        key_count[c] += 1

    result = []
    permutation_with_dups_helper(len(chars), key_count, [], result)
    return result

def permutation_with_dups_helper(goal, key_count, current_seq, result):
    if goal == len(current_seq):
        result.append(current_seq)
        return

    for c, count in key_count.iteritems():
        if count > 0:
            new_seq = deepcopy(current_seq)
            new_seq.append(c)
            key_count[c] = count - 1
            permutation_with_dups_helper(goal, key_count, new_seq, result)
            key_count[c] = count

print permutation_with_dups([1])
print permutation_with_dups([1, 1, 1, 1])
print permutation_with_dups([1, 2, 3])
