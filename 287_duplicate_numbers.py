
dp = [[0 for j in range(7)] for i in range(7)]

for i in range(7): dp[i][0] = 1
for j in range(7): dp[0][j] = 1

for i in range(1, 7):
    for j in range(1, 7):
        dp[i][j] = dp[i-1][j] + dp[i][j-1]


for row in dp: print(*row)
print(dp[-1][-1])
