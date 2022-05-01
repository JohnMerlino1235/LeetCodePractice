class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        max_area = 0

        visited = set()

        rows = len(grid)
        cols = len(grid[0])

        def bfs(r, c):
            q = collections.deque()
            q.append((r, c))
            visited.add((r, c))
            area = 1
            while q:
                x, y = q.popleft()

                for dx, dy in [[0, 1], [1, 0], [-1, 0], [0, -1]]:
                    new_x, new_y = dx + x, dy + y
                    if 0 <= new_x < rows and 0 <= new_y < cols and grid[new_x][new_y] == 1 and (
                    new_x, new_y) not in visited:
                        area += 1
                        q.append((new_x, new_y))
                        visited.add((new_x, new_y))
            return area

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visited:
                    area = bfs(r, c)
                    max_area = max(area, max_area)

        return max_area
