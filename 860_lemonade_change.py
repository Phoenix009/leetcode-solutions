class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        store = {5: 0, 10: 0}
        for bill in bills:
            if bill == 5:
                store[5] += 1
            if bill == 10:
                if store[5] < 1:
                    return False
                store[5] -= 1
                store[10] += 1
            if bill == 20:
                if store[10] >= 1 and store[5] >= 1:
                    store[10] -= 1
                    store[5] -= 1
                elif store[5] >= 3:
                    store[5] -=  # !/usr/bin/env python3
                else:
                    return False
        return True
