from typing import List


class Solution:
    """
    Solution using prefix sums for diagonals

    Time Complexity: O(rows ^ 2 * cols)
    Space Complexity: O(rows * cols)
    """

    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        rows, cols = len(grid), len(grid[0])

        # Precompute the prefix sums for the diagonals
        # dx -> top-left to bottom-right diagonal
        # dy -> top-right to bottom-left diagonal
        dx = [[0] * cols for _ in range(rows)]
        dy = [[0] * cols for _ in range(rows)]

        for r in range(rows):
            for c in range(cols):
                dx[r][c] = grid[r][c] + (dx[r - 1][c - 1] if r > 0 and c > 0 else 0)
                dy[r][c] = grid[r][c] + (
                    dy[r - 1][c + 1] if r > 0 and c < cols - 1 else 0
                )

        rhombus_sums = set()
        for r in range(rows):
            for c in range(cols):
                # Add the single cell as a rhombus of size 1
                rhombus_sums.add(grid[r][c])
                # Fix the the top vertex of the rhombus and try to expand the size
                for size in range(2, rows // 2 + 2):
                    tr, tc = r, c
                    lr, lc = r + size - 1, c - size + 1
                    rr, rc = r + size - 1, c + size - 1
                    br, bc = r + 2 * size - 2, c
                    # Check if the vertices are within bounds
                    if lc < 0 or rc >= cols or br >= rows:
                        break
                    # Calculate the rhombus sum using the precomputed diagonal sums
                    rhombus_sums.add(
                        (dx[rr][rc] - dx[tr][tc])  # Top vertex to Right vertex
                        + (dy[lr][lc] - dy[tr][tc])  # Top vertex to Left vertex
                        + (dy[br][bc] - dy[rr][rc])  # Right vertex to Bottom vertex
                        + (dx[br][bc] - dx[lr][lc])  # Left vertex to Bottom vertex
                        - grid[br][bc]  # Remove the double counted Bottom vertex
                        + grid[tr][tc]  # Add back the double removed Top vertex
                    )
        return sorted(rhombus_sums, reverse=True)[:3]


# Test cases
if __name__ == "__main__":
    solution = Solution()
    print(
        solution.getBiggestThree(
            [
                [3, 4, 5, 1, 3],
                [3, 3, 4, 2, 3],
                [20, 30, 200, 40, 10],
                [1, 5, 5, 4, 1],
                [4, 3, 2, 2, 5],
            ]
        )
    )  # Output: [228, 216, 211]
    print(
        solution.getBiggestThree(
            [
                [1, 2, 3],
                [4, 5, 6],
                [7, 8, 9],
            ]
        )
    )  # Output: [20, 9, 8]
