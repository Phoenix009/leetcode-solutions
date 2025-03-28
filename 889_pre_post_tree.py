

def helper(pre, post):
    if not pre or not post: return None
    
    if len(pre) == 1: return TreeNode(val = pre[0])
    
    root_val = pre[0]
    left_root = pre[1]
    right_root = post[-2]

    if left_root == right_root:
        return TreeNode(val = root_val, left = helper(pre[1:], post[:-1]))
    else:
        index = pre.index(right_root)
        left_pre = pre[1:index]
        right_pre = pre[index:]

        index = post.index(left_root)
        left_post = post[:index+1]
        right_post = post[index+1:-1]

        return TreeNode(
            val = root_val,
            left = helper(left_pre, left_post),
            right = helper(right_pre, right_post),
        )
    


pre = [1,2,4,5,3,6,7]
post = [4,5,2,6,7,3,1]

ans = helper(pre, post)

