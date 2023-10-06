class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        def helper(nums):
            if not nums: return True
            if len(nums) == 1: return False
            if nums[0] == nums[1] and helper(nums[2:]): return True
            if len(nums) >= 3 and nums[0] == nums[1] == nums[2] and helper(nums[3:]): return True
            if len(nums) >= 3 and nums[1] == nums[0] + 1 and nums[2] == nums[1] + 1 and helper(nums[3:]): return True
            return False

        return helper(nums)
