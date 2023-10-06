class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        # import numpy as np
        # matrix = np.array(matrix)
        # return matrix.T.tolist()

        return [col for col in zip(*matrix)]

        
