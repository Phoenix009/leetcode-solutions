def solve(s):

    def helper(ans, length, store):
        if len(ans) == length:
            return True
        if ans == []:
            for alpha in store:
                if store[alpha] == 0:
                    continue
                ans.append(alpha)
                store[alpha] -= 1
                if helper(ans, length, store):
                    return True
                ans.pop()
                store[alpha] += 1
            return False
        else:
            for alpha in store:
                if store[alpha] == 0:
                    continue
                if ans[-1] == alpha:
                    continue
                ans.append(alpha)
                store[alpha] -= 1
                if helper(ans, length, store):
                    return True
                ans.pop()
                store[alpha] += 1
            return False

    from collections import Counter
    frq = Counter(s)
    ans = []
    if helper(ans, len(s), frq):
        return "".join(ans)
    return ""


print(solve("aab"))
print(solve("aaab"))
