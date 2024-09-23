class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        store = dict(zip([chr(ord('a') + i) for i in range(26)], widths))

        lines = 0
        width = 0
        i = 0
        while i < len(s):
            if width + store[s[i]] > 100:
                lines += 1
                width = 0
                continue
            else:
                width += store[s[i]]
                i += 1

        return lines+1, width
