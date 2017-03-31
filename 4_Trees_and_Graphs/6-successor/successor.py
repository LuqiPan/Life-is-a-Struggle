def successor(node):
    if not node:
        return None

    if node.right:
        successor = node.right
        while successor.left: # pay attention
            successor = successor.left

        return successor
    else:
        successor = node.parent
        while successor and successor.right == node:
            node = successor
            successor = successor.parent

        return successor
