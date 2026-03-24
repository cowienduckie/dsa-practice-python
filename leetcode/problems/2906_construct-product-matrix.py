from typing import List


class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        MOD = 12345
        rows, cols = len(grid), len(grid[0])
        prod = [[1] * cols for _ in range(rows)]

        prefix = 1
        for r in range(rows):
            for c in range(cols):
                prod[r][c] = prefix
                prefix = (prefix * grid[r][c]) % MOD

        suffix = 1
        for r in range(rows - 1, -1, -1):
            for c in range(cols - 1, -1, -1):
                prod[r][c] = (prod[r][c] * suffix) % MOD
                suffix = (suffix * grid[r][c]) % MOD

        return prod
