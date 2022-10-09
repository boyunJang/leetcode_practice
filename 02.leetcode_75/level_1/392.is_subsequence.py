class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0: return True
        s_idx = 0
        for i in range(len(t)):
            s_c = s[s_idx]
            t_c = t[i]
            if s_c == t_c:
                s_idx += 1
                if s_idx == len(s):
                    return True
        return False