# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        
        def inorder(root):
            if root.left: yield from inorder(root.left)
            yield root
            if root.right: yield from inorder(root.right)

        
        store = [node.val for node in inorder(root)]
        for node, val in zip(inorder(root), sorted(store)):
            node.val = val

        return root

