class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        from sortedcollections import SortedSet

        if not nums:
            return 0

        nums = SortedSet(nums)
        maxi = 0
        current, count = nums[0], 1

        for num in nums[1:]:
            if num == current + 1:
                current, count = num, count + 1
            else:
                maxi = max(maxi, count)
                current, count = num, 1
        maxi = max(maxi, count)

        return maxi
