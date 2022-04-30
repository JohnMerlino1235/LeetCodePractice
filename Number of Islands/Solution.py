class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        Breadth first search

        """

        if not grid:
            return 0

        num_islands = 0

        rows = len(grid)
        cols = len(grid[0])

        visited = set()

        def bfs(r, c):
            q = collections.deque()
            q.append((r, c))
            visited.add((r, c))

            while q:

                x, y = q.popleft()

                for dx, dy in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                    new_x = x + dx
                    new_y = y + dy
                    if 0 <= new_x < rows and 0 <= new_y < cols and grid[new_x][new_y] == "1" and (
                    new_x, new_y) not in visited:
                        q.append((new_x, new_y))
                        visited.add((new_x, new_y))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    bfs(r, c)
                    num_islands += 1

        return num_islands