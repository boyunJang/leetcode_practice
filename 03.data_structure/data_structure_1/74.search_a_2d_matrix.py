class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            if target < matrix[i][0]: return False
            if target > matrix[i][-1]: continue
            if target in matrix[i] : return True
            else: return False
        return False