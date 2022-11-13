class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        answer = ""
        word1_list = list(word1)
        word2_list = list(word2)
        while len(word1_list) > 0 and len(word2_list) > 0:
            answer = answer + word1_list[0] + word2_list[0]
            word1_list.pop(0)
            word2_list.pop(0)

        if len(word1_list) > 0:
            answer = answer + "".join(word1_list)
        if len(word2_list) > 0:
            answer = answer + "".join(word2_list)

        return answer