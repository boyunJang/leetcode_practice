class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        dic = {}
        for i in range(len(numbers)):
            tmp = numbers[i]
            if target - tmp in dic: return [dic[target - tmp], i + 1]
            dic[tmp] = i + 1