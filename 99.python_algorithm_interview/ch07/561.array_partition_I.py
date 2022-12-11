class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        output = 0
        for i in range(0, len(nums), 2):
            output += nums[i]
        return output