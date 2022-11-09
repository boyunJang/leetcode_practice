class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        max_diff = max(arr) - min(arr)
        if max_diff % (len(arr) - 1) != 0: return False
        diff_rate = max_diff / (len(arr) - 1)
        num = min(arr)
        while num < max(arr):
            num += diff_rate
            if num not in arr: return False
        return True