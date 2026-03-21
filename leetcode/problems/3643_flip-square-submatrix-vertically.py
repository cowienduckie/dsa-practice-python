from typing import List

class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], r0: int, c0: int, k: int) -> List[List[int]]:
        rows, cols = len(grid), len(grid[0])

        for i in range(k // 2):
            for c in range(c0, c0 + k):
                grid[r0 + i][c], grid[r0 + k - 1 - i][c] = grid[r0 + k - 1 - i][c], grid[r0 + i][c]
        
        return grid
