def solve(n):
    ans = 1
    for i in range(1, n):
        ans += 4*i
    return ans


ans = [1, 5, 13, 25, 41, 61, 85, 113, 145, 181, 221]
for i in range(1, len(ans) + 1):
    assert(ans[i-1] == solve(i))


