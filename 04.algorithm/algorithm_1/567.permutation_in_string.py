from collections import Counter, defaultdict

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_dic = Counter(s1)
        s2_dic = defaultdict(int)

        start = 0
        end = 0
        while end < len(s2):
            # print(start, end)
            # print(",".join([key + ":" + str(value) for key, value in s2_dic.items()]))
            c = s2[end]
            end += 1
            if c not in s1_dic:
                while start < end - 1:
                    s2_dic[s2[start]] -= 1
                    if s2_dic[s2[start]] == 0: s2_dic.pop(s2[start])
                    start += 1
                start = end
            else:
                s2_dic[c] += 1
                if s1_dic == s2_dic: return True
                if s2_dic[c] > s1_dic[c]:
                    while s2_dic[c] > s1_dic[c]:
                        s2_dic[s2[start]] -= 1
                        if s2_dic[s2[start]] == 0: s2_dic.pop(s2[start])
                        start += 1
        return False