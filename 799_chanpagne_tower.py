class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        store = [[0 for j in range(100)] for i in range(100)]

        store[0][0] = poured
        
        for i in range(99):
            for j in range(i+1):
                flow = (store[i][j] - 1.0) / 2.0

                if flow > 0:
                    store[i+1][j] += flow
                    store[i+1][j+1] += flow

        return min(1, store[query_row][query_glass])

