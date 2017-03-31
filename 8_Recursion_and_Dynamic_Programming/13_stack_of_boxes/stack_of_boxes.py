def stack_of_boxes(boxes, bottom, offset, memo):
    if offset >= len(boxes):
        return 0

    new_bottom = boxes[offset]
    if not bottom or new_bottom.can_be_top_of(bottom):
        if memo[offset] == 0:
            memo[offset] = stack_of_boxes(boxes, new_bottom, offset + 1, memo)
            memo[offset] += bottom.height

        height_with_new_bottom = memo[offset]

    height_without_new_bottom = stack_of_boxes(boxes, bottom, offset + 1, memo)
    return max(height_with_new_bottom, height_without_new_bottom)
