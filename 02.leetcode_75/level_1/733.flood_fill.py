class Solution:
    def bfs(self, image, sr, sc, color):
        org_color = image[sr][sc]
        if org_color == color: return image
        image[sr][sc] = color
        direction = [[0,1],[1,0],[-1,0],[0,-1]]
        for tmp_dir in direction:
            tr = sr + tmp_dir[0]
            tc = sc + tmp_dir[1]
            if tr >= 0 and tr < len(image) and tc >= 0 and tc < len(image[0]):
                if image[tr][tc] == org_color:
                    image = self.bfs(image, tr, tc, color)
        return image

    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        new_image = self.bfs(image, sr, sc, color)
        return new_image