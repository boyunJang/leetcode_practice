class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        squares = [num ** 2 for num in nums]
        squares.sort()
        return squares