class Solution:
    def smallestNumber(self, pattern: str) -> str:
        def helper(acc, pattern, store):
            if not pattern: return "".join(acc)

            if pattern[-1] == 'I':
                for dig in store:
                    if dig < acc[-1]: continue

                    store.remove(dig)
                    poss, ans = helper(acc + [i], pattern[:-1], store)
                    if poss: return ans
                    store.add(dig)
            else:
                for dig in store:
                    if dig > acc[-1]: continue

                    store.remove(dig)
                    poss, ans = helper(acc + [i], pattern[:-1], store)
                    if poss: return ans
                    store.add(dig)

        n = len(pattern) + 1
        for i in range(1, n + 1):
            store = set(j for j in range(1, n+1) if j != i)
            poss, ans = helper([i], pattern, store)
            if poss: return ans

