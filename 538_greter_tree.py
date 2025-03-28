# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def helper(root, acc):
            if root.right: acc, root.right = helper(root.right, acc)
            root.val += acc
            if root.left: acc, root.left = helper(root.left, acc)
            return acc, root

        return helper(root, 0)[1]

