class Solution:
    def floodFill(
        self, image: List[List[int]], sr: int, sc: int, color: int
        ) -> List[List[int]]:
        from collections import deque

        color_to_fill = image[sr][sc]

        x_diff = [-1, 0, 1, 0]
        y_diff = [0, 1, 0, -1]

        queue = deque()
        queue.append((sr, sc))

        while deque:
            x, y = deque.pop()
            image[x][y] = color

            for x_, y_ in zip(x_diff, y_diff):
                new_x, new_y = x + x_, y + y_
                if not 0 <= new_y <= len(image):
                    continue
                if not 0 <= new_x <= len(image[0]):
                    continue
                if image[new_x][new_y] == color_to_fill:
                    queue.append((new_x, new_y))
        return image

