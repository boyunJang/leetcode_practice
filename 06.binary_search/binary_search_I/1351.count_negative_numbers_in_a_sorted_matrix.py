class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = sum([len([num for num in row if num < 0]) for row in grid])
        return count