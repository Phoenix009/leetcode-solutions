def solve(nums, k):
    if k == 0:
        return 0
    ans = 0

    left = 0
    acc = 1
    for right in range(len(nums)):
        acc *= nums[right]
        while acc >= k and left <= right:
            acc //= nums[left]
            left += 1
        ans += right - left + 1
    return ans


print(solve([10, 5, 2, 6], 100))
print(solve([1, 2, 3], 0))
print(solve([1, 1, 1], 1))
