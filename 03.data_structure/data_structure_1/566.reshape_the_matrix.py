class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        tmp_r = len(mat)
        tmp_c = len(mat[0])
        if tmp_r * tmp_c != r * c : return mat
        r_i = 0
        c_i = 0
        new_mat = [[0 for col in range(c)] for row in range(r)]
        for i in range(tmp_r):
            for j in range(tmp_c):
                new_mat[r_i][c_i] = mat[i][j]
                c_i += 1
                if c_i == c:
                    c_i = 0
                    r_i += 1
        return new_mat