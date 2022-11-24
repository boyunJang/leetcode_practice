class Solution:
    def specialArray(self, nums: List[int]) -> int:
        low = 0
        high = len(nums)
        while low <= high:
            mid = (low + high) // 2
            count = len([num for num in nums if num >= mid])
            if count == mid: return mid
            if count < mid: high = mid - 1
            else: low = mid + 1

        return -1