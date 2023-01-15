class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0: return 0
        start = 0
        end = 0
        max_len = 1
        word_dic = {}
        for idx, c in enumerate(s):
            if c in word_dic:
                repeat_idx = word_dic[c]
                if repeat_idx + 1 > start:
                    start = repeat_idx + 1
            word_dic[c] = idx
            end += 1
            print(c, start, end)
            if end - start > max_len:
                max_len = end - start

        return max_len
