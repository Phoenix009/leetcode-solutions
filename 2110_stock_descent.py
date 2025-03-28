def solve(prices):
    ans = 1
    count = 1
    for price1, price2 in zip(prices, prices[1:]):
        if price2 == price1 - 1: count += 1
        else: count = 1
        ans += count
    
    return ans

solve([3, 2, 1, 4])
solve([8, 6, 7, 7])
solve([1])

