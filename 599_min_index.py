class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:

        store1 = dict(zip(reversed(list1), range(len(list1), 0, -1)))
        store2 = dict(zip(reversed(list2), range(len(list2), 0, -1)))

        res = []
        mini = float('inf')

        for key in store1:
            if key not in store2:
                continue

            value = store1[key] + store2[key]
            if value < mini:
                mini = value
                res = [key]
            elif value == mini:
                res.append(key)

        return res
