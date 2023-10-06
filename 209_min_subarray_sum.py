class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums) < target: return 0

        left, right = 0, 0
        current_sum = 0
        min_length = len(nums)

        while right < len(nums):
            current_sum += nums[right]

            while left <= right and current_sum >= target:
                min_length = min(min_length, right - left + 1)
                current_sum -= nums[left]
                left += 1
            right += 1

        return min_length


