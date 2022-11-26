class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        mat_dic = {}
        for idx in range(len(mat)):
            count = sum(mat[idx])
            if count not in mat_dic:
                mat_dic[count] = []
            mat_dic[count].append(idx)

        answer = []

        for key, value in sorted(mat_dic.items(), key = lambda x:x[0], reverse = False):
            # print(key, value)
            for val in value:
                # print(answer)
                if len(answer) == k: return answer
                answer.append(val)
        return answer