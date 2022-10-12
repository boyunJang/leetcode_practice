from collections import defaultdict

class Solution:
    def longestPalindrome(self, s: str) -> int:
        chr_dic = defaultdict(int)

        for c in s:
            chr_dic[c] += 1

        palin = 0
        odd_exist = 0

        for c, cnt in chr_dic.items():
            if cnt % 2 == 0:
                palin += cnt
            else:
                odd_exist = 1
                palin += int(cnt / 2) * 2

        return palin + odd_exist