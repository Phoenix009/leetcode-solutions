def solve(grid):
    n_rows, n_cols = len(grid), len(grid[-1])

    dp = [[-1 for j in range(n_cols)] for i in range(n_rows)]

    queue = []
    for i in range(n_rows):
        for j in range(n_cols):
            if grid[i][j] == 1:
                queue.append((i, j, 0))
                dp[i][j] = 0

    while queue:
        new_queue = []
        for cx, cy, step in queue:
            for dx, dy in zip([-1, 0, 1, 0], [0, 1, 0, -1]):
                tx, ty = cx + dx, cy + dy
                if tx < 0 or tx >= n_rows or ty < 0 or ty >= n_cols:
                    continue
                if grid[tx][ty] == 2 or dp[tx][ty] != -1:
                    continue
                dp[tx][ty] = step + 1
                new_queue.append((tx, ty, step + 1))

        queue = new_queue
    
    for row in grid: print(*row)
    print()

    for row in dp: print(*row)
    print()

    final_ans = -1
    queue = [(0, 0, 0, 10**9)]
    grid[0][0] = 2
    while queue:
        new_queue = []
        for cx, cy, step, ans in queue:

            if cx == n_rows - 1 and cy == n_cols - 1:
                print(f"possibility, {ans}")
                final_ans = max(final_ans, ans)
                continue

            for dx, dy in zip([-1, 0, 1, 0], [0, 1, 0, -1]):
                tx, ty = cx + dx, cy + dy
                if tx < 0 or tx >= n_rows or ty < 0 or ty >= n_cols:
                    continue
                if grid[tx][ty] == 2 or dp[tx][ty] != -1 and dp[tx][ty] <= step+1:
                    continue

                grid[tx][ty] = 2
                new_queue.append(
                    (tx, ty, step + 1, min(ans, dp[tx][ty] - step - 1)))
                print(new_queue[-1])

        queue = new_queue
    
    print(f"final_ans: {final_ans}")
    if final_ans < -1: return 10**9
    if final_ans == -1: return final_ans
    return final_ans - 1


grid = [[0,0,0],[2,2,0],[1,2,0]]

print(solve(grid))
