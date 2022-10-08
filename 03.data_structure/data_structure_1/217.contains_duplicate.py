class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        num_dic = {}
        for num in nums:
            if num in num_dic:
                return True
            num_dic[num] = 1
        return False