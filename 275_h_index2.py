

def solve(citations):
    lo = 0
    hi = len(citations) - 1

    ans = 0

    while lo <= hi:
        mid = lo + (hi - lo) // 2

        if citations[mid] >= len(nums) - i:
            ans = mid
            lo = mid + 1
        else:
            hi = mid - 1

    return ans

