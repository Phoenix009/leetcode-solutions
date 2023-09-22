
def find_ways(s):
    if not s: return 1
    if s[0] == '0': return 0
    
    if len(s) < 2:
        if 0 < int(s) < 27: return 1
        return 0
    
    ans = find_ways(s[1:])
    if 0 < int(s[:2]) < 27: ans += find_ways(s[2:])
    
    return ans

def solve():
    s = input()
    ans = find_ways(s)
    print(ans)

for t in range(int(input())):
    solve()

