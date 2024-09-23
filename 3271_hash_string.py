

def stringHash(s: str, k: int) -> str:
    def getHash(s):
        acc = 0
        for alpha in s:
            acc += ord(alpha) - ord('a')
        
        acc %= 26
        return chr(ord('a') + acc)

    res = ""
    start_index = 0
    while (start_index < len(s)):
        chunk = s[start_index: start_index+k]
        char = getHash(chunk)
        res += char
        start_index = start_index+k
    return res


print(stringHash("abcd", 2))
print(stringHash("mxz", 3))
