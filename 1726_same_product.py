class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        from collections import defaultdict

        store = defaultdict(int)

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                store[nums[i] * nums[j]] += 1

        ans = 0
        for val in store.values():
            ans += (val * (val - 1)) * 4

        return ans

