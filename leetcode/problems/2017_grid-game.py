from typing import List


class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        # After first bot moves, the second bot can only choose one of two rows leftovers to maximize its score
        # So, at each index i, we compute the maximum sum of (-1, i) on first row and (i, n) on second row
        first_row_sum = sum(grid[0])
        second_row_sum = 0
        ans = float("inf")
        for i in range(len(grid[0])):
            first_row_sum -= grid[0][i]
            ans = min(ans, max(first_row_sum, second_row_sum))
            second_row_sum += grid[1][i]
        return ans
