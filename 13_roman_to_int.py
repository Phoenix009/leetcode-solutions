class Solution:
    def romanToInt(self, s: str) -> int:
        store = {
                'I': 1,
                'IV': 4,
                'V': 5,
                'IX': 9,
                'X': 10,
                'XL': 40,
                'L': 50,
                'XC': 90,
                'C': 100,
                'CD': 400,
                'D': 500,
                'CM': 900,
                'M': 1000,
                }

        result, index = 0, 0
        while index < len(s):
            if index+1 < len(s) and s[index] + s[index+1] in store:
                result += store[s[index] + s[index+1]]
                index += 2
            else:
                result += store[s[index]]
                index += 1
            
        return result
