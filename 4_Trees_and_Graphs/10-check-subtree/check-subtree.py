def pre_order_string(root, result):
    if not root:
        result = result + 'X'
        return

    result = result + str(root.value) + ' '
    pre_order_string(root.left, result)
    pre_order_string(root.right, result)

def contain_tree(needle, haystack):
    needle_s = ''
    pre_order_string(needle, needle_s)
    haystack_s = ''
    pre_order_string(haystack, haystack_s)

    return needle_s in haystack_s
