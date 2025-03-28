class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        from collections import defaultdict
        from queue import deque

        n_nodes = len(edges) + 1

        graph = defaultdict(list)
        for (src, dest) in edges:
            graph[src].append(dest)
            graph[dest].append(src)

        parent = [-1 for i in range(n_nodes)]
        stack = [(-1, 0)]
        while stack:
            prnt, curr_node = stack.pop()
            parent[curr_node] = prnt

            for child in graph[curr_node]:
                stack.append((curr_node, child))


        bob_visited = [-1 for i in range(n_nodes)]
        curr_node, steps = (bob, 0)
        while curr_node != -1:
            bob_visited[curr_node] = steps
            curr_node, steps = parent[curr_node], steps + 1

        stack = [(0, -1, 0, 0)]
        ans = -1
        while stack:
            curr_node, parent, steps, score = stack.pop()

            if bob_visited[curr_node] > steps: score += amount[curr_node]
            elif bob_visited[curr_node] == steps: score += amount[curr_node] // 2
            else: pass

            is_leaf = True
            for node in graph[curr_node]:
                if node == parent: continue
                is_leaf = False
                stack.append((node, curr_node, steps+1, score))

            if is_leaf: ans = max(ans, score)

        return ans





