
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        def helper(inorder, post):
            if not inorder: return None


            root = post[-1]
            root_index = inorder.find(root)
            in_left = inorder[:root_index - 1]
            in_right = inorder[root_index + 1:]

            post_left = postorder[:len(in_left)]
            post_right = postorder[len(in_left):-1]

            print(in_left, in_right)
            print(post_left, post_right)

            return TreeNode(
                val = root_val,
                left = helper(in_left, post_left),
                right = helper(in_right, post_right)
            )
       
