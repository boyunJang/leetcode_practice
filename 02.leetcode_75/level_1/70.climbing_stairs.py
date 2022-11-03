class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1: return 1
        p0, p1 = 1, 1
        answer = 0
        for i in range(2, n + 1):
            answer = p0 + p1
            p0 = p1
            p1 = answer
        return answer