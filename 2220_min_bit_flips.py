def minBitFlips(start: int, goal: int) -> int:
    return bin(start ^ goal)[2:].count('1')

