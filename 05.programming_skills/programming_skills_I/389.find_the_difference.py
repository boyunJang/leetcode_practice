from collections import Counter

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_dic, t_dic = Counter(s), Counter(t)
        for key, value in t_dic.items():
            if key not in s_dic or s_dic[key] != value:
                return key