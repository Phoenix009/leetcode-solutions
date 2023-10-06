class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        stack = rooms[0]

        vis = [0 for i in range(len(rooms))]
        vis[0] = 1

        while stack:
            curr_node = stack.pop()
            if vis[curr_node]:
                continue

            vis[curr_node] = 1
            stack.extend(rooms[curr_node])

        return all(vis)
