class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        def is_self_dividing(num):
            for dig in str(num):
                dig = int(dig)
                if num % dig: return False
            return True

        res = list(filter(is_self_dividing, range(left, right+1)))
        return res


