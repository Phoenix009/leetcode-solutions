class Solution:
    def findLUSlength(self, text1: str, text2: str) -> int:
        if text1 == text2: return -1
        return max(len(text1), len(text2))
