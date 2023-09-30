class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        def division(stack):
            b = stack.pop()
            return int(stack.pop() / b)
        
        operator_store = {
            "+": lambda stack: stack.pop() + stack.pop(),
            "-": lambda stack: -stack.pop() + stack.pop(),
            "*": lambda stack: stack.pop() * stack.pop(),
            "/": division
        }

        for token in tokens:
            stack.append(operator_store.get(token, lambda stack: int(token))(stack))
        return stack[-1]
