
def solve(nums1, nums2):
    from collections import defaultdict
    store = defaultdict(int)

    for idx, val in nums1:
        store[idx] += val

    for idx, val in nums1:
        store[idx] += val

    return list([key, store[key]] for key in sorted(store.keys()))

