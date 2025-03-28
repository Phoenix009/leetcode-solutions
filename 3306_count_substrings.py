def solve(word, k):
    def get_prefix_sum(word, alpha):
        dp = [0]
        for al in word:
            if al == alpha:
                dp.append(dp[-1] + 1)
            else:
                dp.append(dp[-1])
        return dp

    def is_valid(left, right, store):
        right += 1
        count = 0

        for alpha in "aeiou":
            alpha_count = store[alpha][right] - store[alpha][left]
            if alpha_count < 1:
                return -1
            count += alpha_count

        length = right - left
        cons_count = length - count
        print("\t\t", word[left:right], cons_count)
        return cons_count

    def get_max_left(r):
        print(f"\t from get_max_left:")
        ans = None
        left, right = 0, r
        while left <= right:
            mid = left + (right - left) // 2
            cons_count = is_valid(mid, r, store)
            if cons_count < k:
                right = mid - 1
            elif cons_count == k:
                if ans is None:
                    ans = mid
                ans = min(ans, mid)
                right = mid - 1
            else:
                left = mid + 1
        return ans

    def get_min_left(r):
        print(f"\t from get_min_left:")
        ans = None
        left, right = 0, r
        while left <= right:
            mid = left + (right - left) // 2
            cons_count = is_valid(mid, r, store)
            if cons_count < k:
                right = mid - 1
            elif cons_count == k:
                if ans is None:
                    ans = mid
                ans = max(ans, mid)
                left = mid + 1
            else:
                left = mid + 1
        return ans

    store = dict((alpha, get_prefix_sum(word, alpha)) for alpha in "aeiou")
    ans = 0
    for right in range(k-1, len(word)):
        print(f"For right = {right}:")
        min_left = get_max_left(right)
        max_left = get_min_left(right)

        if max_left is None or min_left is None: continue
        ans += max_left - min_left + 1
        print(f"\t min_left = {min_left}, max_left = {max_left}")

        print()
        print()
        print()
    return ans


print(solve("iqeaouqi", 2))
