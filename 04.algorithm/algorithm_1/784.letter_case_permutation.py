class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        if s.isdigit(): return [s]
        alpha = []
        for i, c in enumerate(s):
            if not c.isdigit(): alpha.append(i)

        string = s.lower()

        sol = []
        def get_sol(idx, string):
            if idx != len(alpha):
                if string not in sol: sol.append(string)
                get_sol(idx + 1, string)
                i = alpha[idx]
                string = string[:i] + string[i].upper() + string[i + 1:]
                if string not in sol: sol.append(string)
                get_sol(idx + 1, string)

        get_sol(0, string)

        return sol