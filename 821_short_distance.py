
def calculate_index(s, c):
    pre = []
    char_index = -1

    for i in range(len(s)):
        if s[i] == c:
            char_index = i
        if char_index == -1:
            pre.append(float('inf'))
        else:
            pre.append(abs(i - char_index))
    return pre


def shortestToChar(s: str, c: str):
    pre = calculate_index(s, c)
    pos = calculate_index(s[::-1], c)
    pos = pos[::-1]

    print(pre)
    print(pos)

    res = [min(pr, ps) for (pr, ps) in zip(pre, pos)]
    print(res)
    return res

shortestToChar("loveleetcode", "e")

