from collections import defaultdict

class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        hashmap = defaultdict(int)
        for i in range(len(secret)):
            c = secret[i]
            hashmap[c] += 1

        a, b = 0, 0

        for i in range(len(guess)):
            c = guess[i]
            if c in hashmap and hashmap[c] > 0:
                if c == secret[i]:
                    a += 1
                    hashmap[c] -= 1
        for i in range(len(guess)):
            c = guess[i]
            if c in hashmap and hashmap[c] > 0:
                if c != secret[i]:
                    b += 1
                    hashmap[c] -= 1

        return "%dA%dB" % (a, b)