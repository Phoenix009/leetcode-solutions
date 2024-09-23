def isOneBitCharacter(bits: List[int]) -> bool:
    ans = False
    i = 0
    while (i < len(bits)):
        if bits[i] == 0:
            ans = True
            i += 1
        else:
            ans = False
            i += 2
    return ans

