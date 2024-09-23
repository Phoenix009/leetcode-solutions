def largestNumber(nums):
    from functools import cmp_to_key

    def cmp(a, b):
        outcome1 = int(str(a) + str(b))
        outcome2 = int(str(b) + str(a))

        if outcome1 > outcome2: return -1
        else: return 1
    
    nums.sort(key = cmp_to_key(cmp))
    return str(int("".join(map(str, nums))))




if __name__ == '__main__':
    print(largestNumber([3,30,34,5,9]))
    print(largestNumber([2, 10]))
    print(largestNumber([0, 0]))

