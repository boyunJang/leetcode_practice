import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        r = re.compile('[a-z0-9]+')
        s = "".join(r.findall(s.lower()))

        half_len = len(s) // 2
        front = s[:half_len]
        back = s[half_len:]
        if len(s) % 2 == 1:
            back = back[1:]
        back = "".join(list(reversed(list(back))))
        if front == back: return True
        else: return False