class Solution:
    def judgeCircle(self, moves: str) -> bool:
        from collections import Counter
        frq = Counter(moves)
        return frq.get('U', 0) == frq.get('D', 0) and frq.get('L', 0) == frq.get('R', 0)
