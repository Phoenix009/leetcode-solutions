def get_value(pre):
    index = pre.find('-')
    return int(pre[:index])

def get_partitions(pre, depth):
    i = 0
    while i < len(pre):
        count = 0
        while pre[i] == '-':
            count += 1
            i += 1

        if count == depth:
            left = pre[:i-depth]
            right = pre[i:]
            return left, right
        i += 1

    return pre, ""

# def helper(pre, depth=1):
#     if not pre:
#         return None
#
#     root_val = get_value(pre)
#
#     left, right = get_partitions(pre[1:], depth)
#     print(root_val, left, right)
#
#     return TreeNode(
#         val=root.val,
#         left=helper(left, depth + 1),
#         right=helper(right, depth + 1)
#     )
