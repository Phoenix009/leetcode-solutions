class Solution:
    def reverseVowels(self, s: str) -> str:
        is_vowel = lambda x: x.lower() in "aeiou"
    
        vowels = []
        for alpha in s:
            if is_vowel(alpha): vowels.append(alpha)

        result = ""
        for alpha in s:
            if is_vowel(alpha): result += vowels.pop()
            else: result += alpha
        return result
