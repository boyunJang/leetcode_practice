from collections import Counter

class Solution:
    def firstUniqChar(self, s: str) -> int:
        chr_dic = Counter(s)
        for idx, c in enumerate(s):
            if chr_dic[c] == 1:
                return idx
        return -1