class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        pre = [0]
        for num in nums:
            pre.append(pre[-1] + num)

        max_avg = float("-inf")
        for i in range(k, len(pre)):
            avg = (pre[i] - pre[i-k]) / k
            max_avg = max(max_avg, avg)

        return max_avg
