from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        longest_len = 0
        c_dic = defaultdict(int)
        for r in range(len(s)):
            c_dic[s[r]] += 1

            cells_count = r - l + 1
            if cells_count - max(c_dic.values()) <= k:
                longest_len = max(longest_len, cells_count)

            else:
                c_dic[s[l]] -= 1
                l += 1

        return longest_len