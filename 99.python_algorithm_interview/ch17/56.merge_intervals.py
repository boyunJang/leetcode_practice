class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])

        answer = []
        start, end = -1, -1
        for s, e in intervals:
            if start == -1:
                start, end = s, e
            else:
                if s <= end < e:
                    end = e
                elif s > end:
                    answer.append([start, end])
                    start, end = s, e
        answer.append([start, end])

        return answer