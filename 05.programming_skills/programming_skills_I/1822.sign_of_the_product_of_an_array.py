class Solution:
    def arraySign(self, nums: List[int]) -> int:
        if 0 in nums: return 0
        minus_cnt = len([num for num in nums if num < 0])
        if minus_cnt % 2 == 1: return -1
        return 1