class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        answer = []
        candidates = sorted(candidates)
        def dfs(idx, nlist, nsum):
            if nsum == target:
                answer.append(nlist)
            for i in range(idx, len(candidates)):
                cand = candidates[i]
                if nsum + cand > target: break
                dfs(i, nlist + [cand], nsum + cand)

        dfs(0, [], 0)

        return answer