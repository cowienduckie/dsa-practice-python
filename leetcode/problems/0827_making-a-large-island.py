from typing import List


class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)

        # Helpers
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        def is_valid_cell(r: int, c: int) -> bool:
            return 0 <= r < n and 0 <= c < n

        # Use dfs to spread island number and return its size
        visited = [[False] * n for _ in range(n)]
        island = [[-1] * n for _ in range(n)]
        sizes = []

        def dfs(r: int, c: int) -> int:
            if not is_valid_cell(r, c) or visited[r][c] or grid[r][c] == 0:
                return 0
            visited[r][c] = True
            island[r][c] = len(sizes)
            lands = 1
            for dr, dc in dirs:
                lands += dfs(r + dr, c + dc)
            return lands

        # Loop through the grid to traverse all islands
        for r in range(n):
            for c in range(n):
                if not visited[r][c] and grid[r][c] == 1:
                    sizes.append(dfs(r, c))

        # If there is no island, return 1
        if not sizes:
            return 1

        # Loop through the grid to try flipping every water cell
        # Calculate the size of new island after merging neighbors islands
        ans = max(sizes)
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    continue
                neighbors = {
                    island[r + dr][c + dc]
                    for dr, dc in dirs
                    if is_valid_cell(r + dr, c + dc) and island[r + dr][c + dc] != -1
                }
                ans = max(ans, sum([sizes[i] for i in neighbors]) + 1)

        return ans
