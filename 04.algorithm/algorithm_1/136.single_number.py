from collections import defaultdict

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        num_dic = defaultdict(int)
        for n in nums:
            num_dic[n] += 1

        for key, value in num_dic.items():
            if value == 1: return key