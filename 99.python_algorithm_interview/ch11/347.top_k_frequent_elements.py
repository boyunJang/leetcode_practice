class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        tmp_dic = collections.defaultdict(int)
        for num in nums:
            tmp_dic[num] += 1

        answer = []
        for key, value in sorted(tmp_dic.items(), key = lambda x:x[1], reverse = True):
            answer.append(key)
            if len(answer) >= k: break


        return answer