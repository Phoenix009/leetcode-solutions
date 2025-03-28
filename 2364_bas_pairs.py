class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        from collections import defaultdict

        store = defaultdict(int)

        for index, num in enumerate(nums):
            store[num - index] += 1

        good_pairs = 0
        for val in store.values():
            good_pairs += (val * (val-1)) // 2

        n = len(nums)
        bad_pairs = n * (n-1) // 2
        bad_pairs -= good_pairs
        return bad_pairs
