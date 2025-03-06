from typing import List


class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        duplicated = missing = -1
        checked = [0] * (n * n + 1)

        for r in range(n):
            for c in range(n):
                checked[grid[r][c]] += grid[r][c]

        for i, val in enumerate(checked):
            if val > i:
                duplicated = i
            elif val != i and val == 0:
                missing = i

        return [duplicated, missing]
