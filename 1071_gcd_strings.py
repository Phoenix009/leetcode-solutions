class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
    #    length1, length2 = len(str1), len(str2)
    #    min_length = min(length1, length2)

    #    for length in range(min_length, 0, -1):
    #        quo1, mod1 = length1 // length, length1 % length
    #        quo2, mod2 = length2 // length, length2 % length

    #        if mod1 != 0 or mod2 != 0: continue

    #        prefix = str1[:length]
    #        s1, s2 = prefix * quo1, prefix * quo2

    #        if s1 == str1 and s2 == str2: return prefix

    #    return ""
    
    from math import gcd

    if str1 + str2 != str2 + str1: return ""
    length = gcd(len(str1), len(str2))
    return str1[:length]

