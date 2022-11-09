class Solution:
    def isHappy(self, n: int) -> bool:
        num_dic = {n : 1}
        while True:
            str_n = str(n)
            new_n = sum([int(i) ** 2 for i in str_n])
            if new_n in num_dic:
                if new_n == 1: return True
                else: return False
            num_dic[new_n] = 1
            n = new_n