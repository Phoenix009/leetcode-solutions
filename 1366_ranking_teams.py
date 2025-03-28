def solve(votes):
    from collections import defaultdict
    from functools import cmp_to_key

    def cmp(item1, item2):
        if item1[0] < item2[0]:
            return -1
        elif item1[1] < item2[1]:
            return -1
        return 1

    store = defaultdict(int)

    for vote in votes:
        for index, team in enumerate(vote):
            store[team] += index

    votes = list(store.items())
    votes.sort(key=cmp_to_key(cmp))
    ans = "".join(item[0] for item in votes)
    return ans


print(solve(["ABC","ACB","ABC","ACB"]))
