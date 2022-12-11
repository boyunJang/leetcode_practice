class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        zero_cnt = 0
        for num in nums:
            if num == 0:
                zero_cnt += 1
                if zero_cnt > 1: return [0] * len(nums)
            else: product *= num
        print(product)
        output = []
        for num in nums:
            if zero_cnt > 0:
                if num != 0: output.append(0)
                else: output.append(product)
            else: output.append(product // num)
        return output
