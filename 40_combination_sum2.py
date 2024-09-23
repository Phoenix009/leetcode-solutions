def combinationSum2(candidates, target):
    def helper(nums, target, selected):
        print(f"{nums}, {target}, {selected}")
        if target == 0: yield tuple(sorted(selected))
        else:
            for i, num in enumerate(nums):
                if num > target: break

                # How is this a valid check???
                if i>0 and num == nums[i-1]: continue

                yield from helper(nums[i+1:], target - num, selected + [num])


    candidates.sort()
    result = list(set(helper(candidates, target, [])))
    return result




print(combinationSum2([10,1,2,7,6,1,5], 8))

