class Solution:
    def pivotIndex(self, nums: List[int]) -> int:

        total = sum(nums)
        current_sum = 0
        for i in range(len(nums)):
            tmp_total = total - nums[i]
            if current_sum == tmp_total / 2:
                return i
            current_sum += nums[i]

        return -1