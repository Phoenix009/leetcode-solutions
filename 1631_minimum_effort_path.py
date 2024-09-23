class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:

        low, high = 0, 1e6
        ans = 0
        while low <= high:
            mid = low + (high - low)//2
            if path_finder(matrix, mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return ans
