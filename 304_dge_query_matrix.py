def init(matrix):
    n_rows, n_cols = len(matrix), len(matrix[-1])
    dp = [[0 for j in range(n_cols+1)] for i in range(n_rows + 1)]

    for i in range(1, n_rows + 1):
        for j in range(1, n_cols + 1):
            dp[i][j] = dp[i-1][j] + dp[i][j-1] + matrix[i-1][j-1] - dp[i-1][j-1]

    return dp

def query(row1, col1, row2, col2, dp):
    row1, col1 = row1 + 1, col1 + 1
    row2, col2 = row2 + 1, col2 + 1

    res = dp[row2][col2] - dp[row2][col1 - 1] - dp[row1 - 1][col2] + dp[row1-1][col1-1]
    return res



matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
dp = init(matrix)

for row in dp:
    print(*row)
