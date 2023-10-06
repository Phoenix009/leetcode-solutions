class Solution:

    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        from collections import defaultdict

        def get_path(graph, num, den):

            def helper(graph, src, dest, path, vis):
                if dest == src:
                    return path + [dest]

                vis.add(src)
                for node in graph[src]:
                    if node in vis:
                        continue
                    _path = helper(graph, node, dest, path + [src], vis)
                    if _path:
                        return _path

            if num not in graph:
                return []
            if den not in graph:
                return []

            return helper(graph, num, den, [], set())

        store = {}
        graph = defaultdict(set)

        for (num, den), value in zip(equations, values):
            store[f"{num}-{den}"] = value
            store[f"{den}-{num}"] = 1/value

            graph[num].add(den)
            graph[den].add(num)

        result = []
        for num, den in queries:
            path = get_path(graph, num, den)
            if not path:
                result.append(-1)
                continue

            value = 1
            for num, den in zip(path, path[1:]):
                value *= store[f"{num}-{den}"]
            result.append(value)

        return result

