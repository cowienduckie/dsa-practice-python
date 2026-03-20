from typing import List


class Solution:
    def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
        rows, cols = len(grid), len(grid[0])

        def calc_diff(r0: int, c0: int) -> int:
            # If k is 1, there is only 1 number, so the answer is 0.
            if k == 1:
                return 0
            # Get the unique numbers in the k x k submatrix and sort them.
            arr = sorted(
                set([grid[r][c] for r in range(r0, r0 + k) for c in range(c0, c0 + k)])
            )
            # If there is only 1 unique number, the answer is also 0.
            if len(arr) == 1:
                return 0
            # Otherwise, calculate the minimum absolute difference between any two numbers in the sorted array.
            min_diff = float("inf")
            for i in range(1, len(arr)):
                min_diff = min(min_diff, abs(arr[i] - arr[i - 1]))

            return min_diff

        # Brute-force to calculate the minimum absolute difference for each k x k submatrix.
        return [
            [calc_diff(r, c) for c in range(cols - k + 1)] for r in range(rows - k + 1)
        ]
