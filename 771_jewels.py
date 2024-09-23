class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        from collections import Counter
        frq = Counter(stones)

        res = sum(frq.get(jewel, 0) for jewel in jewels)
        return res
