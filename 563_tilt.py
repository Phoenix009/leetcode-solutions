# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        def helper(root):
            if not root:
                return 0, 0
            left_tilt, left_sum = helper(root.left)
            right_tilt, right_sum = helper(root.right)

            tilt = left_tilt + right_tilt + abs(left_sum - right_sum)
            sum = left_sum + right_sum + root.val
            return tilt, sum

        return helper(root)[0]
