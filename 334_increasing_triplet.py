class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:

        smaller_to_left = []
        stack = []
        for num in nums:
            while stack and stack[-1] >= num: stack.pop()
            smaller_to_left.append(len(stack) > 0)
            stack.append(num)

        greater_to_right = []
        stack = []
        for num in reversed(nums):
            while stack and stack[-1] <= num: stack.pop()
            greater_to_right.append(len(stack) > 0)
            stack.append(num)
        greater_to_right = list(reversed(greater_to_right))

        for i in range(len(nums)):
            if smaller_to_left[i] and greater_to_right[i]: return True

