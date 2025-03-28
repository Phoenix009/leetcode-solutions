class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        from collections import defaultdict

        degrees = [0 for i in range(n)]
        tree = defaultdict(int)

        for src, dest in edges:
            degrees[src] += 1
            degrees[dest] += 1
            tree[src] = dest
            tree[dest] = src

        nodes = [node for node, degree in enumerate(degrees) if degree == 1]
        while (len(nodes) > 2):
            new_nodes = [tree[node] for node in nodes]
            node = new_nodes

        return nodes

        print(nodes)
