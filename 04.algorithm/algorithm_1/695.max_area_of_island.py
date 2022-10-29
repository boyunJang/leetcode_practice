class Solution:
    def inarea(self, tr, tc, R, C):
        if tr >= 0 and tr < R and tc >= 0 and tc < C: return True
        return False

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        R, C = len(grid), len(grid[0])
        visited = [[0 for n in range(C)] for m in range(R)]
        direction = [[1,0],[-1,0],[0,1],[0,-1]]
        for r in range(R):
            for c in range(C):
                if visited[r][c] == 0 and grid[r][c] == 1:
                    queue = [[r, c]]
                    visited[r][c] = 1
                    tmp_area = 1
                    while len(queue) > 0:
                        tr, tc = queue[0]
                        for d in direction:
                            nr = tr + d[0]
                            nc = tc + d[1]
                            if self.inarea(nr, nc, R, C) and visited[nr][nc] == 0 and grid[nr][nc] == 1:
                                tmp_area += 1
                                visited[nr][nc] = 1
                                queue.append([nr, nc])
                        queue.pop(0)
                    max_area = max(max_area, tmp_area)
                visited[r][c] = 1
        return max_area