from collections import Counter


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        sl, pl = len(s), len(p)
        if len(s) < len(p): return []
        answer = []
        hashmap = Counter(p)

        for i in range(pl - 1):
            if s[i] in hashmap: hashmap[s[i]] -= 1

        for i in range(-1, sl - pl + 1):
            if i > -1 and s[i] in hashmap:
                hashmap[s[i]] += 1
            if i + pl < sl and s[i + pl] in hashmap:
                hashmap[s[i + pl]] -= 1

            if all(v == 0 for v in hashmap.values()):
                answer.append(i + 1)

        return answer