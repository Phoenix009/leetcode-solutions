class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        from collections import Counter
        frq = Counter(nums)
        ans = 0
        for count in frq.values():
            ans += (count * (count - 1)) // 2
        return ans
