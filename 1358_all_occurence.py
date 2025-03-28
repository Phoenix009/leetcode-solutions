def solve(s):
    if len(s) < 3: return 0

    dp = [[-1, -1, -1] for i in range(len(s))]

    index = len(s) - 1
    if s[index] == 'a':
        dp[index][0] = index
    if s[index] == 'b':
        dp[index][1] = index
    if s[index] == 'c':
        dp[index][2] = index

    for index in range(len(s)-2, -1, -1):
        dp[index] = dp[index+1][:]
        if s[index] == 'a':
            dp[index][0] = index
        if s[index] == 'b':
            dp[index][1] = index
        if s[index] == 'c':
            dp[index][2] = index

    ans = 0
    for i in range(len(s)):
        if any(val == -1 for val in dp[i]): continue
        right = max(dp[i])
        ans += len(s) - right

    return ans

solve("abcabc")
solve("aaacb")
solve("acb")
