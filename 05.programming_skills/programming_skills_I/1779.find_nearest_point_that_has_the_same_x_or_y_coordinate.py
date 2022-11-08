class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        result = 20000
        idx = -1
        for i, point in enumerate(points):
            a, b = point
            if a != x and b != y: continue
            dist = abs(x - a) + abs(y - b)
            if result > dist:
                result = dist
                idx = i
        return idx