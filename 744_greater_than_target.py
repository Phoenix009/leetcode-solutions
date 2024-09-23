class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        from bisect import bisect_right
        index = bisect_right(letters, target)
        if index == len(letters): return letters[0]
        return letters[index]
