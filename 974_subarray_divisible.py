class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        from collections import defaultdict

        store = [0 for i in range(k)]
        store[0] = 1

        acc = 0
        ans = 0
        for num in nums:
            acc += num
            acc %= k

            store[acc] += 1

            ans += store[acc]

        return ans


