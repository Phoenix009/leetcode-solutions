# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def search_helper(root, val):
            if not root: return None
            if root.val == val: return root
            if val < root.val: return search_helper(root.left, val)
            if val > root.val: return search_helper(root.right, val)

        return search_helper(root, val)
