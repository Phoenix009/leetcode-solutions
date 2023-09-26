# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        def helper(node):
            if node is None: return 0

            left_val = helper(node.left)
            right_val = helper(node.right)
            return left_val + right_val + 1
        
        return helper(root)
