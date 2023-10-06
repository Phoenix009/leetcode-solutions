class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        maxi, current = 0, 0
        for diff in gain:
            current += diff
            maxi = max(maxi, current)
        return maxi

