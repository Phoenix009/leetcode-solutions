def uncommonFromSentences(s1: str, s2: str):
    from collections import Counter
    frq = Counter(s1.split() + s2.split())
    ans = [word for (word, count) in frq.items() if count == 1]
    return ans

print(uncommonFromSentences("this apple is sweet", "this apple is sout"))

