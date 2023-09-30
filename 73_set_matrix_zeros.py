class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        n_rows, n_cols = len(matrix), len(matrix[0])
        rows_flag = [0 in row for row in matrix]
        cols_flag = [0 in col for col in zip(*matrix)]

        for i in range(n_rows):
            for j in range(n_cols):
                if rows_flag[i]: matrix[i][j] = 0
                if cols_flag[j]: matrix[i][j] = 0


