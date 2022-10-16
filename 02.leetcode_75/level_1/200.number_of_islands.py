class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        direction = [[0,1],[0,-1],[1,0],[-1,0]]
        R, C = len(grid), len(grid[0])
        def dfs(r, c):
            grid[r][c] = "2"
            for tmp_dir in direction:
                tmp_r = r + tmp_dir[0]
                tmp_c = c + tmp_dir[1]
                if tmp_r >= 0 and tmp_r < R and tmp_c >= 0 and tmp_c < C:
                    if grid[tmp_r][tmp_c] == "1":
                        dfs(tmp_r, tmp_c)

        for i in range(R):
            for j in range(C):
                if grid[i][j] == "1":
                    count += 1
                    dfs(i, j)

        return count