class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = [[1]]

        if numRows == 1: return result
        
        for row in range(2, numRows + 1):
            res = [1]

            for i in range(row)



