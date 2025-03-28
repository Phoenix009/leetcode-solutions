def solve(candies, k):
    def assign_candies(piles, candy, k):
        if candy == 0:
            return True
        count = 0
        for pile in piles:
            count += pile // candy
            if count >= k:
                return True
        return False

    ans = None
    left, right = 0, sum(candies)//k
    while left <= right:
        mid = left + (right - left) // 2
        if assign_candies(candies, mid, k):
            if ans is None:
                ans = mid
            ans = max(ans, mid)
            left = mid + 1
        else:
            right = mid - 1

    return ans


print(solve([5, 8, 6], 3))
print(solve([2, 5], 11))
