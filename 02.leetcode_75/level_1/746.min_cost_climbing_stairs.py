class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = {}
        dp[0] = 0
        dp[1] = cost[0]
        clen = len(cost)
        for i in range(2, clen + 1):
            dp[i] = min(dp[i-2], dp[i-1]) + cost[i-1]
        return min(dp[clen-1], dp[clen])