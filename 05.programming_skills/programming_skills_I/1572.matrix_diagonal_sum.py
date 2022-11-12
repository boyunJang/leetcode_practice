class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        matlen = len(mat)
        answer = 0
        for i in range(matlen // 2):
            j = matlen - i - 1
            answer += mat[i][i] + mat[i][j] + mat[j][j] + mat[j][i]

        if matlen % 2 == 1:
            half = matlen // 2
            answer += mat[half][half]

        return answer
