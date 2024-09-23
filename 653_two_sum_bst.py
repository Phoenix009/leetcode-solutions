# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        from collections import deque

        vis = set()
        queue = deque(root)

        while queue:
            curr_node = queue.popleft()

            if k - curr_node.val in vis: return True
            vis.add(curr_node.val)

            queue.append(curr_node.left)
            queue.append(curr_node.right)

        return False





