def wordBreak(s, wordDict) -> bool:
    def helper(s, wordDict):
        if len(s) == 0:
            return True
        current_part = ""
        for i in range(len(s)):
            current_part += s[i]
            if current_part in wordDict:
                ans = helper(s[i+1:], wordDict)
                if ans:
                    return ans
        return False
    wordDict = set(wordDict)
    return helper(s, wordDict)



print(wordBreak("leetcode", ["leet", "code"]))
print(wordBreak("catsandog", ["cat", "cats", "sand", "dog"]))
print(wordBreak("applepenapple", ["apple", "pen"]))


