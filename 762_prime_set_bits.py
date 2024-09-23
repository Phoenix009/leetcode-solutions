class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        def is_prime(num):
            for i in range(2, int(num**0.5) + 1):
                if num % i == 0: return False
            return True
        
        count = sum(1 if is_prime(bin(num)[2:].count('1')) else 0 for i in range(left, right+1))
        return count

