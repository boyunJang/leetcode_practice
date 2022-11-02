class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        sol = []
        def backtrack(remain, perm):
            if remain == 0:
                if perm not in sol: sol.append(perm.copy())
            else:
                for i in range(len(nums)):
                    if nums[i] not in perm:
                        perm.append(nums[i])
                        backtrack(remain - 1, perm)
                        perm.pop()
        backtrack(len(nums), [])
        return sol