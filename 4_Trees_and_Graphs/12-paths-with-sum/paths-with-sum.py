from collections import defaultdict

result_count = 0
sum_map = defaultdict(list)
current_running_sum = 0
target_sum = 423

def paths_with_sum(root, depth):
    current_running_sum += root.value
    sum_map[current_running_sum].append(depth)
    if sum_map[current_running_sum - target_sum]:
        result_count += len(sum_map[current_running_sum - target_sum])

    if root.left:
        paths_with_sum(root.left, depth + 1)

    if root.right:
        paths_with_sum(root.right, depth + 1)

    sum_map[current_running_sum].remove(depth)
