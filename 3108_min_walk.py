def solve(n, edges, query):
    def find_parent(parent, node):
        if parent[node] == node:
            return node
        parent[node] = find_parent(parent, parent[node])
        return parent[node]

    def union(parent, size, nodeA, nodeB):
        parentA = find_parent(parent, nodeA)
        parentB = find_parent(parent, nodeB)

        if parentA == parentB:
            return
        if size[parentA] < size[parentB]:
            parentA, parentB = parentB, parentA

        parent[parentB] = parentA
        size[parentA] += parentB

    parent = [i for i in range(n)]
    size = [1 for i in range(n)]

    for (a, b, wt) in edges:
        union(parent, size, a, b)

    acc = dict()
    for (a, b, wt) in edges:
        parentA = find_parent(parent, a)
        if parentA not in acc:
            acc[parentA] = wt
        acc[parentA] &= wt

    ans = []
    for (a, b) in query:
        parentA = find_parent(parent, a)
        parentB = find_parent(parent, b)

        if parentA != parentB:
            ans.append(-1)
        else:
            ans.append(acc[parentA])
    return ans


print(solve(5, [[0, 1, 7], [1, 3, 7], [1, 2, 1]], [[0, 3], [3, 4]]))
print(solve(3, [[0, 2, 7], [0, 1, 15], [1, 2, 6], [1, 2, 1]], [[1, 2]]))
