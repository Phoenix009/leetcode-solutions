def solve(nums):
    from collections import Counter
    frq = Counter(nums)
    return all(val % 2 == 0 for val in frq.values())
