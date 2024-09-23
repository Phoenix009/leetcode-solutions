def isBalanced(root):
    def helper(root):
        if not root: return True, 0
        left_ans, left_val = helper(root.left)
        right_ans, right_val = helper(root.right)

        ans = abs(left_val - right_val) < 2
        ans = ans and left_ans and right_ans
        val = max(left_val, right_val) + 1
        return ans, val




    return helper(root)[0]




