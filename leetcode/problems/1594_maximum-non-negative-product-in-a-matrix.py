class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        MOD = 1_000_000_007
        rows, cols = len(grid), len(grid[0])

        max_prod = [[1] * cols for _ in range(rows)]
        min_prod = [[1] * cols for _ in range(rows)]

        for r in range(rows):
            for c in range(cols):
                curr_max = curr_min = grid[r][c]

                if r == 0:
                    curr_max *= max_prod[r][c - 1]
                    curr_min *= min_prod[r][c - 1]
                elif c == 0:
                    curr_max *= max_prod[r - 1][c]
                    curr_min *= min_prod[r - 1][c]
                else:
                    curr_max *= max(max_prod[r - 1][c], max_prod[r][c - 1])
                    curr_min *= min(min_prod[r - 1][c], min_prod[r][c - 1])

                if grid[r][c] < 0:
                    max_prod[r][c] = curr_min
                    min_prod[r][c] = curr_max
                else:
                    max_prod[r][c] = curr_max
                    min_prod[r][c] = curr_min

        return max_prod[rows - 1][cols - 1] % MOD if max_prod[rows - 1][cols - 1] >= 0 else -1