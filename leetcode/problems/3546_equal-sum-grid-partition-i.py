from typing import List


class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        rows, cols = len(grid), len(grid[0])

        prefix = 0
        grid_sum = sum([sum(grid[r]) for r in range(rows)])

        for r in range(rows):
            for c in range(cols):
                prefix += grid[r][c]
            if prefix == grid_sum - prefix:
                return True
            elif prefix > grid_sum - prefix:
                break

        prefix = 0
        for c in range(cols):
            for r in range(rows):
                prefix += grid[r][c]
            if prefix == grid_sum - prefix:
                return True
            elif prefix > grid_sum - prefix:
                break

        return False
