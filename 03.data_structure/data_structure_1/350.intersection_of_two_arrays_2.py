from collections import defaultdict

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        num1_dic = defaultdict(int)
        for n in nums1:
            num1_dic[n] += 1

        ans_dic = defaultdict(int)
        answer = []
        for n in nums2:
            if n in num1_dic:
                if n in ans_dic and ans_dic[n] == num1_dic[n]: continue
                ans_dic[n] += 1
                answer.append(n)
        return answer