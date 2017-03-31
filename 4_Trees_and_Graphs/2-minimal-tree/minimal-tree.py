class Node:
    def __init__(self, number, left=None, right=None):
        self.number = number
        self.left = left
        self.right = right

def print_tree(node, depth):
    if node:
        print_tree(node.left, depth + 1)
        print '{}:{}'.format(depth, node.number)
        print_tree(node.right, depth + 1)

def minimal_tree(arr, start, end):
    if start > end:
        return None

    if start == end:
        return Node(arr[start])

    mid = (start + end) / 2
    return Node(arr[mid], minimal_tree(arr, start, mid - 1), minimal_tree(arr, mid + 1, end))

def helper(n):
    print_tree(minimal_tree(range(n), 0, n - 1), 0)

helper(7)
