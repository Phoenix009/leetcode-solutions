def solve(s, k):
    store = "".join(map(lambda x: x.upper(), s.split('-')))
    
    print(store)

    start = len(store) % k
    ans = []
    if start: ans = [store[:start]]

    for i in range(start, len(store), k):
        ans.append(store[i: i+k])

    print('-'.join(ans))




s = input()
k = int(input())
solve(s, k)


