def solve(s):
    from string import ascii_lowercase

    def prefix_sum(s, alpha):
        dp = [0]
        for al in s:
            if al == alpha:
                dp.append(dp[-1] + 1)
            else:
                dp.append(dp[-1])
        return dp

    def get_beauty(left, right, store):
        right += 1
        maxi = float('-inf')
        mini = float('inf')
        for alpha in ascii_lowercase:
            count = store[alpha][right] - store[alpha][left]
            if count == 0: continue
            maxi = max(maxi, count)
            mini = min(mini, count)
        print(f"\t {maxi} {mini}")
        return maxi - mini

    store = dict((alpha, prefix_sum(s, alpha)) for alpha in ascii_lowercase)

    ans = 0
    for i in range(len(s)):
        for j in range(i, len(s)):
            print(s[i:j+1])
            val = get_beauty(i, j, store)
            ans += val
    return ans




print(solve("aabcb"))
