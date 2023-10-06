class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num == 1: return False
        from math import sqrt, floor

        divisors = []
        for i in range(2, floor(sqrt(num)) + 1):
            if num % i == 0:
                divisors.append(i)
                divisors.append(num // i)
        return sum(divisors) + 1 == num


