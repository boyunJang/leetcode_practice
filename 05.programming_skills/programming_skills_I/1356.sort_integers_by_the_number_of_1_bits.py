class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        def modify_to_binary(num):
            one_cnt = 0
            while num > 0:
                if num % 2 == 1: one_cnt += 1
                num //= 2
            return one_cnt

        binary_dic = {}
        for num in arr:
            one_cnt = modify_to_binary(num)
            if one_cnt not in binary_dic: binary_dic[one_cnt] = []
            binary_dic[one_cnt].append(num)

        answer = []
        for cnt, num_list in sorted(binary_dic.items(), key = lambda x:x[0], reverse = False):
            num_list.sort()
            answer = answer + num_list

        return answer