class Solution:
    def minDeletions(self, s: str) -> int:
        from collections import Counter
        frq = Counter(s)
        frq = sorted(frq.values(), reverse=True)
        ans = 0
        
        i = 1
        while i < len(frq):
            if frq[i-1] > frq[1]: continue
            diff = (frq[i] - frq[i-1]) + 1
            ans += diff
            frq[i] = frq[i] - diff
            i += 1

            if frq[i-1] == 0: break

        res += sum(frq[j] for j in range(i, len(frq)))
        
        return ans
