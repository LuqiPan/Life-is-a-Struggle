from random import randint

def get_random_node(root):
    random_number = randint(0, root.tree_size - 1)

    if random_number == 0:
        return root

    left_tree_size = root.left.tree_size if root.left else 0
    right_tree_size = root.right.tree_size if root.right else 0

    if random_number <= left_tree_size:
        return get_random_node(root.left)
    else:
        return get_random_node(root.right)
