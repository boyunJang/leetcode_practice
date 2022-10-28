class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0: return 0
        max_len = 1
        start = 0
        end = 0
        char_dic = {}
        char_dic[s[start]] = 1
        while end < len(s) - 1:
            end += 1
            if s[end] in char_dic:
                while s[start] != s[end]:
                    char_dic.pop(s[start])
                    start += 1
                start += 1
            else:
                char_dic[s[end]] = 1
            max_len = max(max_len, end - start + 1)

        return max_len