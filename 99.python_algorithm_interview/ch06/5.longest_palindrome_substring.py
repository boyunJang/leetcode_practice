class Solution:
    def longestPalindrome(self, s: str) -> str:
        palin = s[0]
        for i in range(len(s)):
            tmp_palin = s[i]
            center = s[i]
            # 홀수 팰린드롬
            left, right = i, i
            while True:
                left = left - 1
                right = right + 1
                if left < 0 or right >= len(s): break
                if s[left] == s[right]:
                    tmp_palin = s[left] + tmp_palin + s[right]
                else:
                    break
            if len(tmp_palin) > len(palin): palin = tmp_palin
            # 짝수 팰린드롬
            if i + 1 < len(s) and center == s[i + 1]:
                tmp_palin = s[i:i + 2]
                left, right = i, i + 1
                while True:
                    left = left - 1
                    right = right + 1
                    if left < 0 or right >= len(s): break
                    if s[left] == s[right]:
                        tmp_palin = s[left] + tmp_palin + s[right]
                    else:
                        break
                if len(tmp_palin) > len(palin): palin = tmp_palin
        return palin
