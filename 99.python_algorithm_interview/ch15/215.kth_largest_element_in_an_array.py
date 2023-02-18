class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        Q = []
        for num in nums:
            heapq.heappush(Q, -num)

        while k:
            k -= 1
            tmp = heapq.heappop(Q)
            if k == 0: return -tmp

        return -1