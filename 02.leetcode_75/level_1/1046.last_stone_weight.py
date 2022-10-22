from heapq import *
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # stones.sort()
        heap = []
        for stone in stones:
            heappush(heap, -stone)
        while len(heap) > 1:
            x = -heappop(heap)
            y = -heappop(heap)
            # print(x, y)
            if x == y: continue
            else: heappush(heap, -abs(x - y))
        if len(heap) == 0: return 0
        else: return -heap[0]