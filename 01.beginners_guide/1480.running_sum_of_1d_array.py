class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        running_sum = [0] + nums
        for i in range(1, len(nums)+1):
            running_sum[i] += running_sum[i-1]
        return running_sum[1:]