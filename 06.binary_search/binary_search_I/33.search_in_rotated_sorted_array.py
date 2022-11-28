class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if target not in nums: return -1
        min_idx = nums.index(target)
        return min_idx