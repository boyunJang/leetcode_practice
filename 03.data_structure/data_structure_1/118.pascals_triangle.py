class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pascal = [[1]]
        for i in range(1, numRows):
            arr = [0] * (i + 1)
            for j in range(i + 1):
                if j == 0 or j == i:
                    arr[j] = 1
                else:
                    arr[j] = pascal[i - 1][j - 1] + pascal[i - 1][j]
            pascal.append(arr)

        return pascal