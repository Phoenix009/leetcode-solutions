class Solution:
    def findLHS(self, nums: List[int]) -> int:
        from collections import Counter
        frq = Counter(nums)

        maxi = 0
        for key in frq:
            if key + 1 in frq:
                maxi = max(maxi, frq[key] + frq[key+1])

        return maxi
