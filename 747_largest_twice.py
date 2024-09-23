class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        largest, largest2 = 0, 1
        if nums[1] > nums[0]: largest, largest2 = 1, 0

        for i in range(2, len(nums)):
            if nums[i] > nums[largest]:
                largest, largest2 = i, largest
            elif nums[i] > nums[largest2]:
                largest2 = i

        if nums[largest] >= 2*nums[largest2]: return 1
        return -1
