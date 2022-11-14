class Solution:
    def freqAlphabets(self, s: str) -> str:
        answer = []
        for c in s:
            if c == "#":
                tmp = answer.pop()
                tmp = answer.pop() + tmp
                answer.append(tmp)
            else: answer.append(c)
        return "".join([chr(int(c) + 96) for c in answer])