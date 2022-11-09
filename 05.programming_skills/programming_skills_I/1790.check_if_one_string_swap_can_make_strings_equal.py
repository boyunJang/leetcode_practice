from collections import defaultdict

class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2: return True
        # s1_dic = defaultdict(int)
        # s2_dic = defaultdict(int)
        # for c in s1: s1_dic[c] += 1
        # for c in s2: s2_dic[c] += 1
        # if s1_dic != s2_dic: return False
        for i in range(len(s1)):
            s1_c = s1[i]
            s2_c = s2[i]
            if s1_c != s2_c:
                # print(s1_c)
                if s1_c not in s2: return False
                idx = i + 1
                while idx < len(s1):
                    j = s2.index(s1_c, idx)
                    if s1[j] != s1_c: break
                    idx = j + 1
                if idx >= len(s1): return False
                new_s1 = s1[:i] + s1[j] + s1[i+1:j] + s1[i] + s1[j+1:]
                if new_s1 == s2: return True
                else: return False