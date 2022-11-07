class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        product = 1
        sum_result = 0

        while n > 0:
            tmp_num = n % 10
            product *= tmp_num
            sum_result += tmp_num
            n = n // 10

        return product - sum_result