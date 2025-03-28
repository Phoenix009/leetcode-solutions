def solve(n):
    from math import log, floor
    pow = floor(log(n, 3))

    for i in range(pow, -1, -1):
        if 3**i <= n:
            n -= 3**i
            print(i, n)
        if n == 0:
            return True
    return False


print(solve(11))

