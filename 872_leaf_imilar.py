# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def get_leaves(root):
            if not root.left and not root.right: yield root.val
            if root.left: yield from get_leaves(root.left)
            if root.right: yield from get_leaves(root.right)

        l1 = list(get_leaves(root1))
        l2 = list(get_leaves(root2))

        return l1 == l2
