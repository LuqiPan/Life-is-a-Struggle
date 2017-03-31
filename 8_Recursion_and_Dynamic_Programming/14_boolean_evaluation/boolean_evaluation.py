from copy import deepcopy
from pprint import pprint

memo = {
    '1:1': 1,
    '0:0': 1,
    '1:0': 0,
    '0:1': 0,
}

def boolean_evaluation(expression, target, memo):
    if memo.has_key(expression + ':' + str(target)):
        return memo[expression + ':' + str(target)]

    ways = 0
    for delim in range(1, len(expression), 2):
        op = expression[delim]
        left_expression = expression[:delim]
        right_expression = expression[delim + 1:]

        left_true = boolean_evaluation(left_expression, 1, memo)
        left_false = boolean_evaluation(left_expression, 0, memo)
        right_true = boolean_evaluation(right_expression, 1, memo)
        right_false = boolean_evaluation(right_expression, 0, memo)
        total = (left_true + left_false) * (right_true + right_false)

        total_true = 0
        if op == '&':
            total_true = left_true * right_true

        if op == '|':
            total_true = left_true * right_true + left_true * right_false + left_false * right_true

        if op == '^':
            total_true = left_true * right_false + left_false * right_true

        total_false = total - total_true
        sub_ways = total_true if target else total_false
        ways += sub_ways

    if not memo.has_key(expression + ':' + str(target)):
        memo[expression + ':' + str(target)] = ways

    return ways

print boolean_evaluation("1^0|0|1", 0, deepcopy(memo))
print boolean_evaluation("0&0&0&1^1|0", 1, deepcopy(memo))
