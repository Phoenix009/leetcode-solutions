def solve(s):
    from pprint import pprint
    print = pprint
    from string import ascii_lowercase
    from collections import defaultdict

    def get_prefix_sum(s, alpha):
        dp = [0]
        for al in s:
            if al == alpha:
                dp.append(dp[-1] + 1)
            else:
                dp.append(dp[-1])
        return dp

    def get_count(alpha, store, left, right):
        return store[alpha][right+1] - store[alpha][left]

    store = dict()
    for alpha in ascii_lowercase:
        store[alpha] = get_prefix_sum(s, alpha)

    indices = defaultdict(list)
    for index, alpha in enumerate(s):
        if len(indices[alpha]) < 2:
            indices[alpha].append(index)
        else:
            indices[alpha][-1] = index

    ans = 0
    for end in ascii_lowercase:
        if len(indices[end]) < 2:
            continue
        left, right = indices[end]
        left += 1
        right -= 1

        for mid in ascii_lowercase:
            if get_count(mid, store, left, right):
                ans += 1

    return ans


print(solve("aabca"))
print(solve("adc"))
print(solve("bbcbaba"))
