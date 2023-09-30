class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        def is_increasing(arr):
            for i in range(1, len(arr)):
                if arr[i-1] > arr[i]: return False
            return True
        
        return is_increasing(nums) or is_increasing(nums[::-1])


