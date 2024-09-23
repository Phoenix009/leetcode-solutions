class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        neg = list(sorted(filter(lambda x: x < 0, nums)))
        pos = list(sorted(filter(lambda x: x > 0, nums)))
        zero_flg = bool(filter(lambda x: x == 0, nums))

        for i in range(min(k, len(neg))):
            neg[i] *= -1

        k -= min(k, len(neg))

        if k % 2 and not zero_flg:
            pos[0] *= - 1

        return sum(pos) + sum(neg)
