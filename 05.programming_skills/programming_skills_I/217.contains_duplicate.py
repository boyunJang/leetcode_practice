from collections import Counter

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        num_dic = Counter(nums)
        for key, value in sorted(num_dic.items(), key = lambda x:x[1], reverse = True):
            if value > 1: return True
            else: return False
        return False