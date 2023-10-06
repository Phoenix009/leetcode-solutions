class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        pre = [0]
        for num in nums:
            if num == 0: pre.append(0)
            else: pre.append(pre[-1] + 1)

        pos = [0]
        for num in reversed(nums):
            if num == 0: pos.append(0)
            else: pos.append(pos[-1] + 1)
        pos = list(reversed(pos))
        
        maxi = 0
        for i in range(len(nums)):
            current = pre[i] + pos[i+1]
            maxi = max(maxi, current)
        return maxi
