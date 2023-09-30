class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        from heapq import heappush, heappop, heapify

        nums = [-1 * num for num in nums]
        heapify(nums)
        for _ in range(k-1):
            heappop(nums)

        return heappop(nums) * -1
            

