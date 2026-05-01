from typing import List


class Solution:
    def maxPathScore(self, grid: List[List[int]], k: int) -> int:
        rows, cols = len(grid), len(grid[0])

        # Use memo[r][c][i] stores the max path score to reach cell (r, c) with exactly 'i' non-zero values along the path.
        # Initialize with -1 to represent unreachable states.
        memo = [[[-1] * (k + 1) for _ in range(cols)] for _ in range(rows)]
        memo[0][0][1 if grid[0][0] else 0] = grid[0][0]

        # Iterate through the grid and check max path value ending at each (r, c) cell (within k non-zero cell at max)
        for r in range(rows):
            for c in range(cols):
                # Skip first initialized cell
                if r == 0 and c == 0:
                    continue

                curr_value = grid[r][c]
                curr_cost = 1 if curr_value else 0

                for i in range(curr_cost, k + 1):
                    if i - curr_cost >= 0:
                        prev_value = -1
                        # Check path from above
                        if r > 0 and memo[r - 1][c][i - curr_cost] != -1:
                            prev_value = max(prev_value, memo[r - 1][c][i - curr_cost])
                        # Check path from left
                        if c > 0 and memo[r][c - 1][i - curr_cost] != -1:
                            prev_value = max(prev_value, memo[r][c - 1][i - curr_cost])

                        # If a valid path exists from either direction, add the current value.
                        memo[r][c][i] = (
                            curr_value + prev_value if prev_value != -1 else -1
                        )
                    else:
                        memo[r][c][i] = -1

        # Return the maximum score achievable at the destination cell (bottom-right).
        # We check all possible number of non-zero values up to k.
        return max(memo[rows - 1][cols - 1])


if __name__ == "__main__":
    print(Solution().maxPathScore([[0, 2, 2], [1, 1, 1], [0, 0, 2]], 3))
