class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        prefix = [1]
        for num in nums: prefix.append(prefix[-1] * num)
        
        suffix = [1]
        for num in reversed(nums): suffix.append(suffix[-1] * num)
        suffix = list(reversed(suffix))
        
        print(prefix)
        print(suffix)
        
        res = []

        for i in range(len(nums)):
            res.append(prefix[i] * suffix[i+1])
        return res

