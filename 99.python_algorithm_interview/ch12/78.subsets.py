class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        answer = []

        def dfs(idx, nlist):
            answer.append(nlist)
            for i in range(idx, len(nums)):
                num = nums[i]
                dfs(i + 1, nlist + [num])

        dfs(0, [])

        return answer