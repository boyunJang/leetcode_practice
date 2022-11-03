class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        prev_arr = triangle[0]
        new_arr = triangle[0]
        for i in range(2, len(triangle) + 1):
            new_arr = [0] * i
            new_arr[0] = prev_arr[0] + triangle[i-1][0]
            new_arr[-1] = prev_arr[-1] + triangle[i-1][-1]
            for j in range(1, i - 1):
                new_arr[j] = min(prev_arr[j-1], prev_arr[j]) + triangle[i-1][j]
            # print(new_arr)
            prev_arr = new_arr
        return min(new_arr)