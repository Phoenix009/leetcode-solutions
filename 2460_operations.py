def solve(nums):
    for i in range(1, len(nums)):
        if nums[i-1] == nums[i]:
            nums[i-1] *= 2
            nums[i] = 0

    res = [num for num in nums if num > 0]
    res = res + [0 for i in range(len(nums) - len(res))]
    return res
