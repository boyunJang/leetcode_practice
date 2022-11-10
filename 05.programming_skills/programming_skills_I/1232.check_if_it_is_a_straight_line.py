class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        coordinates.sort(key = lambda x:x[1])

        y_dist = coordinates[-1][1] - coordinates[0][1]

        if y_dist == 0: return True

        coordinates.sort(key = lambda x:x[0])

        x_dist = coordinates[-1][0] - coordinates[0][0]

        if x_dist == 0: return True

        y_dist = coordinates[-1][1] - coordinates[0][1]

        total_ratio = float(y_dist) / float(x_dist)

#         print(coordinates)

        for i in range(len(coordinates) - 1):
            x_tmp_gap = coordinates[i + 1][0] - coordinates[i][0]
            y_tmp_gap = coordinates[i + 1][1] - coordinates[i][1]
#             print(x_tmp_gap, y_tmp_gap)
            if x_tmp_gap == 0 or y_tmp_gap == 0: return False
            tmp_ratio = float(y_tmp_gap) / float(x_tmp_gap)
            if tmp_ratio != total_ratio: return False

        return True