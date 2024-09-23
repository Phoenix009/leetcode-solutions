class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        n_rows, n_cols = len(img), len(img[-1])
        res = []

        for i in range(n_rows):
            row = []
            for j in range(n_cols):
                rows = min(n_rows, i+3)
                cols = min(n_rows, i+3)
                row.append(sum(img[i_][j_] for i_ in range(i, rows)
                           for j_ in range(j, cols)) // ((rows-i)*(cols-j)))
            res.append(row)
        return res
