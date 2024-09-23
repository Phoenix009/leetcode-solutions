class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        from collections import defaultdict
        store = defaultdict(lambda: {'count': 0, 'first': -1, 'last': -1})

        for index, num in enumerate(nums):
            store[num]['count'] += 1
            if store[num]['first'] == -1: store[num]['first'] = index
            else: store[num]['last'] = index


        res = 0
        maxi_count = 0
        for value in store.values():
            if value['count'] > maxi_count:
                maxi_count = value['count']
                res = value['last'] - value['first'] + 1

        return res
