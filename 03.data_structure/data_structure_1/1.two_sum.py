from collections import Counter

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            hashmap[nums[i]] = i
        for i in range(len(nums)):
            tmp = nums[i]
            other = target - tmp
            if other in hashmap and hashmap[other] != i:
                return [hashmap[other], i