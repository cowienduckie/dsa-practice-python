from collections import deque
from typing import List


class Solution:
    def highestPeak(self, is_water: List[List[int]]) -> List[List[int]]:
        rows, cols = len(is_water), len(is_water[0])
        grid = [[-1] * cols for _ in range(rows)]

        # Helpers
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        def is_valid_cell(r: int, c: int) -> bool:
            return 0 <= r < rows and 0 <= c < cols

        # Use a queue to store updated cells
        queue = deque()

        # Set the water cells first
        for r in range(rows):
            for c in range(cols):
                if is_water[r][c]:
                    grid[r][c] = 0
                    queue.append((r, c))

        # Spread the land cells by waves
        # For each waves, only set height for unreached ones and add them to queue
        # Wave's height is increased by 1 also.
        curr_height = 1
        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                for dr, dc in dirs:
                    nr = r + dr
                    nc = c + dc
                    if is_valid_cell(nr, nc) and grid[nr][nc] == -1:
                        grid[nr][nc] = curr_height
                        queue.append((nr, nc))
            curr_height += 1

        return grid
