class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:

        from collections import defaultdict


        def add_color(color, colors, ans):
            if colors[color] == 0: ans += 1
            colors[color] += 1
            return ans

        def remove_color(color, colors, ans):
            colors[color] -= 1
            if colors[color] == 0:  ans -= 1
            return ans

        colors = defaultdict(int)
        ball_colors = [0 for i in range(limit + 1)]
        ans = 0
        res = []

        for (ball, color) in queries:
            if ball_colors[ball] == 0:
                ball_colors[ball] = color
                ans = add_color(color, colors, ans)
            else:
                ans = remove_color(ball_colors[ball], colors, ans)
                ball_colors[ball] = color
                ans = add_color(color, colors, ans)
            res.append(ans)

        return res



