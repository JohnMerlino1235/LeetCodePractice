class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        """
        Output -> 2D array, grid cooridates, where result[i] = [r, c]

        """

        rows = len(heights)
        cols = len(heights[0])
        pacific = set()
        atlantic = set()

        def dfs(r, c, visited, previous_height):
            if (r, c) in visited or r < 0 or c < 0 or r == rows or c == cols or heights[r][c] < previous_height:
                return
            visited.add((r, c))
            dfs(r + 1, c, visited, heights[r][c])
            dfs(r - 1, c, visited, heights[r][c])
            dfs(r, c + 1, visited, heights[r][c])
            dfs(r, c - 1, visited, heights[r][c])

        for r in range(rows):
            dfs(r, 0, pacific, heights[r][0])
            dfs(r, cols - 1, atlantic, heights[r][cols - 1])

        for c in range(cols):
            dfs(0, c, pacific, heights[0][c])
            dfs(rows - 1, c, atlantic, heights[rows - 1][c])

        ans = []

        for r in range(rows):
            for c in range(cols):
                if (r, c) in pacific and (r, c) in atlantic:
                    ans.append((r, c))

        return ans