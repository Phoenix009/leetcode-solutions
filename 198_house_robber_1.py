def rob(nums):
    dp = [[0, 0] for i in range(len(nums) + 1)]
    for i in range(1, len(nums) + 1):
        # if i rob this house
        dp[i][1] = nums[i-1]
        dp[i][1] += max(*dp[i-2]) if i-2 > -1 else 0

        # if i dont rob this house
        dp[i][0] = max(*dp[i-1])

    return max(*dp[-1])


print(rob([1, 2, 3, 1]))
print(rob([2, 7, 9, 3, 1]))
