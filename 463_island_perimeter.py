class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        # def bfs(x, y, grid):
        #     grid[x][y] = -1
        #     x_diff = [-1, 0, 1, 0]
        #     y_diff = [0, 1, 0, -1]

        #     peri = 0
        #     for x_, y_ in zip(x_diff, y_diff):
        #         new_x, new_y = x + x_, y + y_
        #         if not 0 <= new_x < len(grid): peri += 1
        #         elif not 0 <= new_y < len(grid[0]): peri += 1
        #         elif grid[new_x][new_y] == 0: peri += 1
        #         elif grid[new_x][new_y] == 1:
        #             peri += bfs(new_x, new_y, grid)
        #     print(f"for {x, y}, peri: {peri}")
        #     return peri
        
        # for i in range(len(grid)):
        #     for j in range(len(grid[i])):
        #         if grid[i][j] == 1:
        #             return bfs(i, j, grid)
        # return 0
        
        peri = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    peri += 4
                    if i > 0 and grid[i-1][j] == 1: peri -= 2
                    if j > 0 and grid[i][j-1] == 1: peri -= 2
        return peri

