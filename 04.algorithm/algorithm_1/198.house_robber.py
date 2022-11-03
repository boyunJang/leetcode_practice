class Solution:
    def rob(self, nums: List[int]) -> int:
        numlen = len(nums)
        if numlen == 1: return nums[0]
        if numlen == 2: return max(nums)
        if numlen == 3: return max(nums[0] + nums[2], nums[1])
        dp = [nums[0], nums[1], nums[0] + nums[2]] + [0] * (numlen - 3)
        for i in range(3, numlen):
            dp[i] = max(dp[i - 2], dp[i - 3]) + nums[i]
        return max(dp)