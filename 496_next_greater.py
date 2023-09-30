class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        store = {}
        stack = []
        for num in reversed(nums2):
            while stack and stack[-1] <= num: stack.pop()
            if not stack: store[num] = -1
            else: store[num] = stack[-1]
            stack.append(num)
        
        res = [store[num] for num in nums1]
        return res