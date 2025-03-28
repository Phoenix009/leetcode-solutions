def solve(n, edges):
    def find_parent(node, parents):
        if parents[node] == node:
            return node
        parents[node] = find_parent(parents[node], parents)
        return parents[node]

    def union_set(nodeA, nodeB, parents, size, acc):
        parentA = find_parent(nodeA, parents)
        parentB = find_parent(nodeB, parents)

        if parentA == parentB:
            return parentA

        if size[parentA] < size[parentB]:
            parentA, parentB = parentB, parentA

        parents[parentB] = parentA
        size[parentA] += size[parentB]
        acc[parentA] += acc[parentB]
        return parentA

    parents = [i for i in range(n)]
    size = [1 for i in range(n)]
    acc = [0 for i in range(n)]

    for src, dst in edges:
        parent = union_set(src, dst, parents, size, acc)
        acc[parent] += 1

    # print(parents)
    # print(size)
    # print(acc)
    #
    ans = 0
    for node in range(n):
        if node == parents[node]:
            if acc[node] * 2 == size[node] * (size[node] - 1):
                ans += 1

    return ans


print(solve(6, [[0, 1], [0, 2], [1, 2], [3, 4]]))
print(solve(6, [[0, 1], [0, 2], [1, 2], [3, 4], [3, 5]]))
print(solve(5, [[1,2],[3,4],[1,4],[2,3],[1,3],[2,4]]))
