class Solution:
    def reverseWord(self, s: str) -> str:
        c_list = [""] * len(s)
        for i in range(len(s) // 2):
            j = len(s) - 1 - i
            c_list[i] = s[j]
            c_list[j] = s[i]
        if len(s) % 2 == 1:
            c_list[len(s) // 2] = s[len(s) // 2]
        return "".join(c_list)

    def reverseWords(self, s: str) -> str:
        tokens = s.split(" ")
        return " ".join([self.reverseWord(token) for token in tokens])