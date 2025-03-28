def isArraySpecial(nums: List[int]) -> bool:
    return all(a&1 != b&1 for a, b in zip(nums, nums[1:]))


