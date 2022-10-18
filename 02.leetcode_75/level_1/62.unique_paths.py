class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1: return 1
        if n == 1: return 1
        prev_arr = [1] * n
        new_arr = [1] * n
        for i in range(1, m):
            for j in range(1, n):
                new_arr[j] = prev_arr[j] + new_arr[j-1]
            prev_arr = new_arr
        return prev_arr[n-1]