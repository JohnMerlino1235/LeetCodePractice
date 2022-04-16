class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        m = len(image)
        n = len(image[0])
        visited = [[False for i in range(m + 1)] for j in range(n + 1)]

        def flip_color(image, x, y, new_color, old_color):
            if (x < 0) or (x >= m) or (y < 0) or (y >= n):
                return
            if visited[x][y] or image[x][y] != old_color:
                return

            visited[x][y] = True
            image[x][y] = new_color
            flip_color(image, x + 1, y, new_color, old_color)
            flip_color(image, x - 1, y, new_color, old_color)
            flip_color(image, x, y + 1, new_color, old_color)
            flip_color(image, x, y - 1, new_color, old_color)

        flip_color(image, sr, sc, newColor, image[sr][sc])
        return image