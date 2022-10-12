class Solution:
    def get_sub_idx(self, i, j):
        sub_idx = 0
        if i >= 3 and i < 6:
            sub_idx += 3
        elif i >= 6:
            sub_idx += 6
        if j >= 3 and j < 6:
            sub_idx += 1
        elif j >= 6:
            sub_idx += 2
        return sub_idx

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_sum = {}
        col_sum = {}
        sub_sum = {}
        for i in range(9):
            row_sum[i] = []
            col_sum[i] = []
            sub_sum[i] = []
        # for cross_sum, start point (0,0) is index 0, otherwise 1
        # cross_sum = {}
        # cross_sum[0] = []
        # cross_sum[1] = []

        for i in range(9):
            for j in range(9):
                n = board[i][j]
                if n == ".": continue
                # check cross_sum
                # if i == j:
                #     if n in cross_sum[0]: return False
                #     cross_sum[0].append(n)
                # elif i + j == 8:
                #     if n in cross_sum[1]: return False
                #     cross_sum[1].append(n)
                # check row_sum
                if n in row_sum[i]: return False
                row_sum[i].append(n)
                # check col_sum
                if n in col_sum[j]: return False
                col_sum[j].append(n)
                # check sub_sum
                sub_idx = self.get_sub_idx(i, j)
                if n in sub_sum[sub_idx]: return False
                sub_sum[sub_idx].append(n)

        return True