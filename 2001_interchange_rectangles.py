class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        from collections import Counter
        frq = Counter(width/height for (width, height) in rectangles)
        ans = sum((count*(count-1))//2 for count in frq.values())
        return ans
