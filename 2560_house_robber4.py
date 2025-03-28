def solve(nums, k):
    from math import ceil

    def is_valid(nums, maxi, k):
        ans = 0
        count = 0
        for num in nums:
            if num <= maxi:
                count += 1
            else:
                ans += ceil(count / 2)
                count = 0

        ans += ceil(count / 2)
        return ans >= k

    left, right = min(nums), max(nums)

    ans = None
    while left <= right:
        mid = left + (right - left) // 2
        if is_valid(nums, mid, k):
            if not ans:
                ans = mid
            ans = min(ans, mid)
            right = mid - 1
        else:
            left = mid + 1

    return ans


print(solve([2, 3, 5, 9], 2))
print(solve([2, 7, 9, 3, 1], 2))
