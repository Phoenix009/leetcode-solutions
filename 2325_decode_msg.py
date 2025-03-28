def solve(key, message):
    from strings import ascii_lowercase

    store = {}

    index = 0
    for alpha in key:
        if alpha in ascii_lowercase:
            if alpha not in store: 
                store[index] = alpha
                index += 1


    res = []
    for alpha in message:
        res.append(store[ord(alpha) - ord('a')])

    return "".join(res)
