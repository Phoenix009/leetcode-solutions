class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        nums_10 = set(int(num, 2) for num in nums)
        for i in range(1 << len(nums)):
            if i not in nums_10: 
                ans = bin(i)[2:]
                ans = "0"*(max(0, len(nums) - len(ans))) + ans
                return ans
