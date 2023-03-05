class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def binarysearch(s_x, s_y, e_x, e_y):
            if s_x <= e_x and s_y <= e_y:
                m_x = s_x + (e_x - s_x) // 2
                m_y = s_y + (e_y - s_y) // 2
                if matrix[m_x][m_y] == target: return True
                elif matrix[m_x][m_y] < target:
                    return binarysearch(m_x + 1, s_y, e_x, e_y) or binarysearch(s_x, m_y + 1, e_x, e_y)
                else:
                    return binarysearch(s_x, s_y, m_x - 1, e_y) or binarysearch(s_x, s_y, e_x, m_y - 1)
            else:
                return False


        answer = binarysearch(0, 0, len(matrix) - 1, len(matrix[0]) - 1)
        return answer