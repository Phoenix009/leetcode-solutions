class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        def possible(word, store):
            for alpha in word:
                if alpha not in store:
                    return False
            return True

        rows = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]
        res = []
        for word in words:
            for row in rows:
                if possible(word, row):
                    res.append(word)
        return res
