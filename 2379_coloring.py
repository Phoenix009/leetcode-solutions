def solve(blocks, k):
    n = len(blocks)

    whites = [0]

    for block in blocks:
        if block == 'W':
            whites.append(whites[-1] + 1)
        else:
            whites.append(whites[-1])

    ans = float('inf')
    for i in range(n - k + 1):
        left = i
        right = i + k 
        ans = min(ans, whites[right] - whites[left])

    return ans

solve("WBBWWBBWBW", 5)
