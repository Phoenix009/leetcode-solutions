def solve(nums):
    ans = 0
    for i in range(len(nums)):
        if nums[i] == 0:
            if i+2 >= len(nums):
                return -1
            nums[i] = (nums[i] + 1) % 2
            nums[i + 1] = (nums[i + 1] + 1) % 2
            nums[i + 2] = (nums[i + 2] + 1) % 2
            ans += 1
    return ans


print(solve([0, 1, 1, 1, 0, 0]))
print(solve([0, 1, 1, 1]))
