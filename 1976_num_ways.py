def solve(n, roads):
    MOD = 10**9 + 7
    from heapq import heappush, heappop

    graph = [set() for i in range(n)]
    for (src, dst, wt) in roads:
        graph[src].add((dst, wt))
        graph[dst].add((src, wt))

    dist = [float('inf') for i in range(n)]
    dist[0] = 0

    ways = [0 for i in range(n)]
    ways[0] = 1

    heap = [(0, 0)]
    while heap:
        currnode, currdist = heappop(heap)
        if currdist > dist[currnode]: continue

        for dst, wt in graph[currnode]:
            if dist[dst] > dist[currnode] + wt:
                dist[dst] = dist[currnode] + wt
                ways[dst] = ways[currnode]
                heappush(heap, (dst, dist[dst]))
            elif dist[dst] == dist[currnode] + wt:
                ways[dst] = (ways[dst] + ways[currnode]) % MOD

    return ways[-1]




print(solve(7, [[0, 6, 7], [0, 1, 2], [1, 2, 3], [1, 3, 3], [
      6, 3, 3], [3, 5, 1], [6, 5, 1], [2, 5, 1], [0, 4, 5], [4, 6, 2]]))

print(solve(2, [[1, 0, 10]]))

print(solve(5, [[0,1,1],[1,2,4],[0,4,3],[3,2,5],[3,4,1],[3,0,5],[1,3,1]]))
