from typing import List


class Solution:
    def countUnguarded(
        self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]
    ) -> int:
        matrix = [[0] * n for _ in range(m)]

        # Mark the walls and guards as INF
        for r, c in walls:
            matrix[r][c] = float("inf")

        for r, c in guards:
            matrix[r][c] = float("inf")

        # Spread the guard's vision in matrix
        def spread_col(col: int, rows: List[int]) -> None:
            for row in rows:
                if matrix[row][col] == float("inf"):
                    break
                matrix[row][col] += 1

        def spread_row(row: int, cols: List[int]) -> None:
            for col in cols:
                if matrix[row][col] == float("inf"):
                    break
                matrix[row][col] += 1

        for r, c in guards:
            spread_col(c, range(r + 1, m))
            spread_col(c, range(r - 1, -1, -1))
            spread_row(r, range(c + 1, n))
            spread_row(r, range(c - 1, -1, -1))

        # Count 0-cells in the matrix as answer
        ans = 0
        for r in range(m):
            for c in range(n):
                if matrix[r][c] == 0:
                    ans += 1

        return ans
