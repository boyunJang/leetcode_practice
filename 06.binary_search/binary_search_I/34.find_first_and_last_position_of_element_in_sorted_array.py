class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        low = 0
        high = len(nums) - 1

        start = len(nums)

        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                start = min(start, mid)
                high = mid - 1
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1

        low = 0
        high = len(nums) - 1
        end = -1

        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                end = max(end, mid)
                low = mid + 1
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1

        if start == len(nums): start = -1

        return [start, end]

