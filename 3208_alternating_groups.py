def solve(colors, k):
    n = len(colors)
    if n < k:
        return 0

    dp = [1 for i in range(len(colors))]

    for i in range(1, k-1):
        if colors[i] != colors[i-1]:
            dp[i] = dp[i-1] + 1
        else:
            dp[i] = 1

    index = k-1
    ans = 0

    for _ in range(n):
        current_index = index % n
        prev_index = (index - 1) % n

        if colors[current_index] != colors[prev_index]:
            dp[current_index] = dp[prev_index] + 1
        else:
            dp[current_index] = 1

        if dp[current_index] >= k:
            ans += 1

        index += 1
    return ans


print(solve([0, 1, 0, 1, 0], 3))
print(solve([0, 1, 0, 0, 1, 0, 1], 6))
print(solve([1, 1, 0, 1], 4))
