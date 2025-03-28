# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        def level_order(root):
            queue = [root]
            
            while queue:
                yield queue

                new_level = []
                for node in queue:
                    if node.left: new_level.append(node.left)
                    if node.right: new_level.append(node.right)

                queue = new_level
        
        if not root: return []
        ans = []
        for level in level_order(root):
            ans.append(level[-1])
        return ans


        
