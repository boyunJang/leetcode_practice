from collections import defaultdict


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine_dic = defaultdict(int)
        for c in magazine:
            magazine_dic[c] += 1

        for c in ransomNote:
            if c not in magazine_dic or magazine_dic[c] == 0:
                return False
            magazine_dic[c] -= 1
        return True