def solve(n):
    n -= 1
    from heapq import heappush, heappop

    ans = 1
    heap2 = [2]
    heap3 = [3]
    heap5 = [5]

    visited = set([1, 2, 3, 5])
    
    while n:
        ans = min(heap2[0], heap3[0], heap5[0])

        if ans == heap2[0]:
            heappop(heap2)

        elif ans == heap3[0]:
            heappop(heap3)

        elif ans == heap5[0]:
            heappop(heap5)

        if ans * 2 not in visited:
            heappush(heap2, ans * 2)
            visited.add(ans*2)

        if ans * 3 not in visited:
            heappush(heap3, ans * 3)
            visited.add(ans*3)

        if ans * 5 not in visited:
            heappush(heap5, ans * 5)
            visited.add(ans*5)
        
        n -= 1
    return ans

print(solve(1))
print(solve(10))
