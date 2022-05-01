class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        """
        Output -> 2D array, grid cooridates, where result[i] = [r, c]

        """

        rows = len(heights)
        cols = len(heights[0])
        pacific = []
        atlantic = []
        visited = set()
        answer = []

        def bfs(r, c):
            cycle = set()
            q = collections.deque()
            q.append((r, c))
            visited.add((r, c))
            cycle.add((r, c))

            while q:
                x, y = q.popleft()
                height = heights[x][y]
                for dx, dy in [[1, 0], [-1, 0], [0, -1], [0, 1]]:
                    new_x, new_y = x + dx, y + dy
                    if new_x < 0 or new_y < 0:
                        pacific.append((r, c))
                        if (r, c) in atlantic and (r, c) not in answer:
                            answer.append((r, c))
                    elif new_y >= cols or new_x >= rows:
                        atlantic.append((r, c))
                        if (r, c) in pacific and (r, c) not in answer:
                            answer.append((r, c))
                    elif height >= heights[new_x][new_y] and (new_x, new_y) not in cycle:
                        q.append((new_x, new_y))
                        cycle.add((new_x, new_y))

        for r in range(rows):
            for c in range(cols):
                if (r, c) not in visited:
                    bfs(r, c)

        return answer

