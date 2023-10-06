class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = "aeiou"
        pre = [0]
        for char in s:
            pre.append(pre[-1])
            pre[-1] += 1 if char in vowels else 0

        print(pre)

        max_count = 0
        for i in range(k, len(pre)):
            count = pre[i] - pre[i-k-1]
            max_count = max(max_count, count)

        return max_count

