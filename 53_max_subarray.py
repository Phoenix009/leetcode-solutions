class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [0]
        for num in nums:
            dp.append(max(dp[-1] + num, num))

        return max(dp)
