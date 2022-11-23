class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        miss_list = [num for num in range(1, max(arr) + k + 1) if num not in arr]
#         print(miss_list)
        return miss_list[k - 1]