class Solution:
    def checkIfExist(self, A: List[int]) -> bool:
        if A.count(0) > 1: return True
        S = set(A) - {0}
        for a in A:
            if 2*a in S: return True
        return False