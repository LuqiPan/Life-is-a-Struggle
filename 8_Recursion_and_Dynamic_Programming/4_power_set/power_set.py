from copy import deepcopy

def power_set(set):
    if not set:
        return [[]]
    sub_power_set = power_set(set[0:-1])
    sub_power_set_copy = deepcopy(sub_power_set)

    for elem in sub_power_set_copy:
        elem.append(set[-1])

    return sub_power_set + sub_power_set_copy

print power_set([1])
print power_set([1, 2])
print power_set([1, 2, 3])
