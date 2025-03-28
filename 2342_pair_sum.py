class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        from collections import defaultdict

        store = defaultdict([])

        for num in nums:
            key = sum(map(int, list(str(num))))
            store[key].append(num)

        ans = -1
        for values in store.values():
            if len(values) > 1:
                ans = max(ans, sum(sorted(values)[-2:]))
        return ans

