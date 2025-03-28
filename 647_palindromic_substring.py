def solve(s):
    n = len(s)

    dp = [[0 for i in range(n)] for j in range(n)]
    
    for j in range(len(s)):
        x, y = (0, j)
        while x < n and y < n:
            if x == y: dp[x][y] = 1
            elif abs(x - y) == 1: dp[x][y] = int(s[x] == s[y])
            else: dp[x][y] = int(s[x] == s[y] and dp[x+1][y-1])
            x += 1
            y += 1
    
    ans = 0
    for row in dp: ans  += sum(row)
    print(ans)
    return ans


solve("abx")

