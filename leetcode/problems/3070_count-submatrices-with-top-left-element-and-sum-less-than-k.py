from typing import List


class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        rows, cols = len(grid), len(grid[0])

        # Convert original grid to prefix sum array where:
        # grid[r][c] = sum of the submatrix from (0, 0) to (r-1, c-1)
        count = 0
        for r in range(rows):
            # Early break if the sum of the submatrix from (0, 0) to (r-1, 0) is already greater than k
            if grid[r][0] > k or (r > 0 and grid[r - 1][0] > k):
                break
            for c in range(cols):
                # Update the current cell to be the sum of the submatrix from (0, 0) to (r-1, c-1)
                grid[r][c] += grid[r - 1][c] if r > 0 else 0
                grid[r][c] += grid[r][c - 1] if c > 0 else 0
                grid[r][c] -= grid[r - 1][c - 1] if r > 0 and c > 0 else 0
                # Check if the sum of the submatrix from (0, 0) to (r-1, c-1) is valid
                # Otherwise, early break since all larger submatrices will also be invalid
                if grid[r][c] <= k:
                    count += 1
                else:
                    break
        return count
