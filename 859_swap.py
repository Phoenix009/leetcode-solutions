def buddyStrings(s: str, goal: str) -> bool:
    s, goal = list(s), list(goal)
    if len(s) != len(goal):
        return False
    mismatch = [i for i in range(len(s)) if s[i] != goal[i]]

    if len(mismatch) > 2:
        return False
    s[mismatch[0]], s[mismatch[1]] = s[mismatch[1]], s[mismatch[0]]
    return s == goal

print(buddyStrings("ab", "ba"))
