class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        from collections import Counter
        frq = Counter(nums)
        thresh = len(nums) // 3
        
        res = []
        for key, count in frq.items():
            if count > thresh: res.append(key)

        return res
        
