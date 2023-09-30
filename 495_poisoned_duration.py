class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        res = 0
        start, end = 0, -1
        for time in timeSeries:
            if start <= time <=end:
                end = time + duration - 1
            else:
                res += end - start + 1
                start = time
                end = time + duration - 1
        res += end - start + 1
        return res
        