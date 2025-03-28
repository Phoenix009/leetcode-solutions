def solve(nums):

    ans = 1
    for i in range(len(nums)):
        count = 1
        acc = nums[i]
        j = i+1
        while j < len(nums) and acc & nums[j] == 0:
            acc = acc | nums[j]
            count += 1
            j += 1
            ans = max(ans, count)
    return ans



print(solve([1, 3, 8, 48, 10]))
print(solve([3, 1, 5, 11, 13]))
