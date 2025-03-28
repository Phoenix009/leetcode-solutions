def solve(nums, queries):
    def apply_queries(nums, queries):
        dp = [0 for i in range(len(nums) + 1)]
        for i, j, val in queries:
            dp[i] += val
            dp[j+1] -= val

        acc = 0
        for i in range(len(nums)):
            acc += dp[i]
            dp[i] = acc

        ans = list(max(0, nums[i] - dp[i]) == 0 for i in range(len(nums)))
        return all(ans)

    ans = None
    left, right = 1, len(queries)
    while left <= right:
        mid = left + (right - left) // 2
        if apply_queries(nums, queries[:mid]):
            if not ans:
                ans = mid
            ans = min(ans, mid)
            right = mid - 1
        else:
            left = mid + 1

    if ans is None:
        return -1
    return ans


print(solve([2, 0, 2], [[0, 2, 1], [0, 2, 1], [1, 1, 3]]))
print(solve([4, 3, 2, 1], [[1,3,2],[0,2,1]]))
