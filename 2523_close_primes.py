def solve(left, right):

    def get_primes(n):
        is_prime = [1 for i in range(right + 1)]

        for i in range(2, n + 1):
            if is_prime[i]:
                yield i
                j = 1
                while j * i <= n:
                    is_prime[i*j] = 0
                    j += 1

    primes = get_primes(right)
    if len(primes) < 2:
        return [-1, -1]

    ans = [-float('inf'), float('inf')]

    for a, b in zip(primes, primes[1:]):
        if not (left <= a <= right) or not (left <= b <= right): continue
        if b-a < ans[1] - ans[0]: ans = [a, b]
    
    return ans


solve(2, 100)
