class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        word_dic = {}
        for word in strs:
            sort_word = str(sorted(word))
            if sort_word not in word_dic:
                word_dic[sort_word] = []
            word_dic[sort_word].append(word)

        answer = []
        for key, value in word_dic.items():
            answer.append(value)

        return answer