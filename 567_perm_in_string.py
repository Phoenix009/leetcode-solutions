def checkInclusion(s1: str, s2: str) -> bool:
    if len(s2) < len(s1): return False

    from collections import Counter
    from collections import defaultdict
    frq = Counter(s1)

    current_frq = defaultdict(int)

    while i < len(s2):
        if i < len(s1): current_frq[s2[i]] += 1
        if i >= len(s1)-1:
            if current_frq == frq: return True
            frq[s2[i - (len(s1) - 1)]] -= 1


    






print(checkInclusion("ab", "eidbaooo"))
print(checkInclusion("ab", "eidboaoo"))

