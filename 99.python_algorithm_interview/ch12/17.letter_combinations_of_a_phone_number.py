class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "" : return []
        answer = []
        nums = {"2" : "abc", "3" : "def", "4" : "ghi", "5" : "jkl", "6" : "mno", "7" : "pqrs", "8" : "tuv", "9" : "wxyz"}

        def dfs(idx, prev):
            if idx == len(digits):
                answer.append(prev)
                return
            for c in nums[digits[idx]]:
                dfs(idx + 1, prev + c)

        dfs(0, "")

        return answer