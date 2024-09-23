class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        pre = [1]
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]: pre.append(pre[-1] + 1)
            else: pre.append(1)
        return max(pre)
