from collections import defaultdict

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = re.sub("[!?',;.]", " ", paragraph.lower())
        paragraph = paragraph.split()
        max_cnt = 0
        max_word = paragraph[0]

        word_dic = defaultdict(int)
        for word in paragraph:
            if word not in banned:
                word_dic[word] += 1
                if word_dic[word] > max_cnt:
                    max_cnt = word_dic[word]
                    max_word = word

        return max_word