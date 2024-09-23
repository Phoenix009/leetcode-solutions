def diffWaysToCompute(expression):
    from queue import deque

    def get_trees(expression):
        found_symbol = False
        for index, alpha in enumerate(expression):
            if alpha not in "-+*":
                continue
            for left in get_trees(expression[:index]):
                for right in get_trees(expression[index+1:]):
                    yield {'val': alpha, 'left': left, 'right': right}
            found_symbol = True

        if not found_symbol:
            yield {'val': expression, 'left': None, 'right': None}

    def post_order(root):
        if root['left']:
            yield from post_order(root['left'])
        if root['right']:
            yield from post_order(root['right'])
        yield root['val']

    ans = []
    for tree in get_trees(expression):
        stack = deque()
        for alpha in post_order(tree):
            if alpha == '-':
                stack.append(-stack.pop() + stack.pop())
            elif alpha == '+':
                stack.append(stack.pop() + stack.pop())
            elif alpha == '*':
                stack.append(stack.pop() * stack.pop())
            else:
                stack.append(int(alpha))
        ans.append(stack.pop())
    return list(ans)


print(diffWaysToCompute("2-1-1"))
print(diffWaysToCompute("2*3-4*5"))
