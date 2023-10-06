class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        from collections import Counter

        for sym in "!?',;.":
            paragraph = paragraph.replace(sym, " ")

        words = []
        for word in paragraph.split():
            word = word.lower()
            words.append(word)

        frq = Counter(words)

        for word in banned:
            if word in frq: frq.pop(word)

        print(frq)

        max_count = 0
        res = ""

        for key, val in frq.items():
            if val > max_count:
                max_count = val
                res = key

        return res
