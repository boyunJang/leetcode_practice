# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        start = 1
        end = n
        min_bad = n
        while start <= end:
            mid = (start + end) // 2
            if isBadVersion(mid):
                if mid < min_bad:
                    min_bad = mid
                end = mid - 1
            else:
                start = mid + 1
        return min_bad