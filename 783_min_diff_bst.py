# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        def inorder(root):
            if root.left: yield from inorder(root.left)
            yield root.val
            if root.right: yield from inorder(root.right)

        values = list(inorder(root))
        res = float('inf')
        for i in range(1, len(values)):
            res = min(res, values[i] - values[i-1])
        
        return res
