
def solve(arr):
    def helper(a, b, store):
        count = None
        while a + b in store:
            if not count: count = 2
            count += 1
            a, b = b, a+b
        return count


    if len(arr) <= 2: return 0

    store = set(arr)

    ans = 0
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            ans = max(ans, helper(arr[i], arr[j], store))

    return ans 





def main():
    nums = list(map(int, input().split()))
    print(solve(nums))

