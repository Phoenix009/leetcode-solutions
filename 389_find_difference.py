class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        from collections import Counter
        from string import ascii_lowercase as alphabets

        frq1 = Counter(s)
        frq2 = Counter(t)

        for alpha in alphabets:
            if frq1[alpha] != frq2[alpha]:
                return alpha





