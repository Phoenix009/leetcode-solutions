class Solution:
    def validPalindrome(self, s: str) -> bool:
        def helper(left, right, s, skipped):
            if left >= right: return True
            if s[left] != s[right]: return helper(left, right-1, s, True) or helper(left+1, right, s, True)
            else: return helper(left+1, right-1, s, skipped)

        return helper(0, len(s)-1, s, False)
