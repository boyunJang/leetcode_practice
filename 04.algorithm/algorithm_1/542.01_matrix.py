class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        if len(mat) == 0: return mat
        m, n = len(mat), len(mat[0])
        dp = [[m * n for i in range(n)] for j in range(m)]

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    dp[i][j] = 0
                else:
                    if i > 0:
                        dp[i][j] = min(dp[i][j], dp[i - 1][j] + 1)
                    if j > 0:
                        dp[i][j] = min(dp[i][j], dp[i][j - 1] + 1)

        for ni in range(m):
            for nj in range(n):
                i, j = m - ni - 1, n - nj - 1
                if i < m - 1:
                    dp[i][j] = min(dp[i][j], dp[i + 1][j] + 1)
                if j < n - 1:
                    dp[i][j] = min(dp[i][j], dp[i][j + 1] + 1)

        return dp