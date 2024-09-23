def maxPossibleScore(start, d):
    def check(start, score, mini, maxi, minindex, maxindex):
        lo, hi = mini + score, maxi - score
        if lo > hi: lo, hi = hi, lo
        for index, num in enumerate(start):
            if index in (minindex, maxindex):
                continue
            print(f"{num} <= {lo} <= {hi} <= {num + d}")
            if not (num <= lo <= hi <= num + d):
                return False
        print(score)
        return True

    lo = min(start)
    minindex = start.index(lo)
    hi = max(start)
    maxindex = start.index(hi)
    hi += d

    ans = -1
    while lo <= hi:
        mid = lo + (hi - lo)//2
        if check(start, mid, lo, hi, minindex, maxindex):
            ans = mid
            lo = mid + 1
        else:
            hi = mid - 1

    return ans


print(maxPossibleScore([6, 0, 3], 2))
print(maxPossibleScore([2, 6, 13, 13], 5))
