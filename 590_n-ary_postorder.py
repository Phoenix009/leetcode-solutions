def postorder(root):
    def _postorder(root):
        if not root: yield
        for child in root.children:
            yield from _postorder(child)
        yield root.val
    return list(_postorder(root))



