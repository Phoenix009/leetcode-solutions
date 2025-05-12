def solve(root):
    store = []
    max_depth = 0

    if not root:
        return None
    
    print(helper(root, 0))


def helper(root, depth):
    if not root:
        return None, depth

    leftLCA, leftDepth = helper(root.left, depth+1)
    rightLCA, rightDepth = helper(root.right, depth+1)

    if leftDepth == rightDepth:
        return leftDepth, root.val
    elif leftDepth > rightDepth:
        return leftDepth, leftLCA
    else:
        return rightDepth, rightLCA
