class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        ans = []
        stack = []

        for i in range(len(temperaturs)-1, -1, -1):
            while stack:
                if tempartures[stack[-1]] > temperatures[i]:
                    ans.append(stack[-1] - i + 1)
                    break
                stack.pop()


                if not stack: ans.append(-1)
                stack.append(i)

        return ans

        
