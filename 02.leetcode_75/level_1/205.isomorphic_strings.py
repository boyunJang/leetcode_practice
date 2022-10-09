class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_word_dic = {}
        t_word_dic = {}
        for i in range(len(s)):
            s_c = s[i]
            t_c = t[i]
            if s_c in s_word_dic and s_word_dic[s_c] != t_c:
                return False
            if t_c in t_word_dic and t_word_dic[t_c] != s_c:
                return False
            if s_c not in s_word_dic:
                s_word_dic[s_c] = t_c
            if t_c not in t_word_dic:
                t_word_dic[t_c] = s_c

        return True