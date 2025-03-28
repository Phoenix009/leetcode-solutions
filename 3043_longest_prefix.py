from pprint import pprint
print = pprint

def longestCommonPrefix(arr1, arr2):

    if len(arr1) < len(arr2): arr1, ar2 = ar2, arr1

    def insert(root, word):
        current_node = root
        for alpha in word:
            if alpha not in current_node: current_node[alpha] = {}
            current_node = current_node[alpha]
        return root

    def traverse(root, word):
        count = 0
        current_node = root
        for alpha in word:
            if alpha not in current_node: return count
            current_node = current_node[alpha]
            count += 1
        return count

    root = {}
    for word in map(str, arr1):
        root = insert(root, word)

    ans = 0
    for word in map(str, arr2):
        ans = max(ans, traverse(root, word))
    return ans

print(longestCommonPrefix([1,10,100], [100]))
print(longestCommonPrefix([1, 2, 3], [4, 4, 4]))
