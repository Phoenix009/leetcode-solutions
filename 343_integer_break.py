class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [1]
        for i in range(2, n+1):
            curr_max = float('-inf')
            for j in range(1, i+1):
                curr_max = max(curr_max, j * dp[i-j])
            dp.append(curr_max)
        return dp[n]



