class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        ans = 0
        for height in heights:
            count = 1
            while stack and stack[-1] >= height:
                stack.pop()
                count += 1

            ans = max(ans, height * count)

        heights = heights[::-1]
        stack = []
        for height in heights:
            count = 1
            while stack and stack[-1] >= height:
                stack.pop()
                count += 1

            ans = max(ans, height * count)

        return ans


