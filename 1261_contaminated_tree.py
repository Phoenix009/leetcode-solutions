
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        def traverse(root):
            yield root.val
            if root.left: yield from traverse(root.left)
            if root.right: yield from traverse(root.right)

        def fix_tree(root):
            
            def helper(root):
                if not root: return None
                if root.left: root.left.val = root.val * 2  + 1
                if root.right: root.right.val = root.val * 2  + 2
                root.left = helper(root.left)
                root.right = helper(root.right)
                return root

            root.val = 0
            root = helper(root)
            return root
            
        root = fix_tree(root)
        self.store = set()
        if root:
            self.store = set(traverse(root))

    

    def find(self, target: int) -> bool:
       return target in self.store


