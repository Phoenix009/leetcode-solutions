from itertools import product, permutations
from collections import Counter
from math import factorial
import string


def countGoodIntegers(n: int, k: int) -> int:
    def get_palindromes(n):
        if n == 1:
            for i in map(int, list(string.digits)):
                yield i
        else:
            repeat = n // 2
            for perm in product(string.digits, repeat=repeat):
                if perm[0] == '0':
                    continue
                chunk = ''.join(perm)

                if n % 2:
                    for i in range(10):
                        yield int(f"{chunk}{i}{chunk[::-1]}")
                else:
                    yield int(f"{chunk}{chunk[::-1]}")

    def countPermutations(num):
        num = str(num)
        frq = Counter(num)
        ans = factorial(len(num))
        for i in frq.keys():
            ans //= factorial(frq[i])

        if frq['0']:
            rem = factorial(len(num) - 1)
            for i in frq.keys():
                if i == '0' and frq[0] > 1:
                    rem //= (frq[i] - 1)
                else:
                    rem //= frq[i]

            ans -= rem
        return ans

    acc = set()
    for i in get_palindromes(n):
        if i % k == 0:
            acc |= set(int("".join(perm))
                       for perm in permutations(str(i)) if perm[0] != '0')

    return len(acc)


# print(countGoodIntegers(3, 5))
# print(countGoodIntegers(1, 4))
# print(countGoodIntegers(5, 6))
print(countGoodIntegers(7, 2))
