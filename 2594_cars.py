def solve(ranks, cars):
    from math import floor

    def is_valid(ranks, cars, time_required):
        count = 0
        for rank in ranks:
            c = floor((time_required // rank) ** 0.5)
            count += c
        return count >= cars

    left = 0
    right = max(ranks) * cars * cars

    ans = None
    while left <= right:
        mid = left + (right - left) // 2
        if is_valid(ranks, cars, mid):
            ans = mid
            right = mid - 1
        else:
            left = mid + 1
    return ans


print(solve([4, 2, 3, 1], 10))
print(solve([5, 1, 8], 6))
