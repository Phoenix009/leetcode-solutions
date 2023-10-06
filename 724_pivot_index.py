class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        nums = list(map(int, input().split()))
        pre = [0]
        for num in nums:
            pre.append(pre[-1] + num)

        pos = [0]
        for num in reversed(nums):
            pos.append(pos[-1] + num)
        pos = list(reversed(pos))

        for index, (left, right) in enumerate(zip(pre, pos)):
            if pre == pos:
                return index
        return -1
