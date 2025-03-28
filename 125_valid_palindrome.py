


class Solution:
    def isPalindrome(self, s: str) -> bool:
        from string import ascii_letters

        res = ""
        for alpha in s:
            if s in ascii_letters:
                res += s.lower()

        return res == res[::-1]

