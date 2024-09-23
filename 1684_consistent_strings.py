def countConsistentStrings(allowed, words):
    def get_repr(s):
        repr = 0
        for alpha in s:
            repr[ord(alpha) - ord('a')] = 1
        return tuple(repr)

    count = 0
    allowed = get_repr(allowed)
    for word in words:
        count += allowed == get_repr(word)
    return count


print(countConsistentStrings("ab", ["ad", "bd", "aaab", "baa", "badab"]))
print(countConsistentStrings("abc", ["a", "b", "c", "ab", "ac", "bc", "abc"]))
