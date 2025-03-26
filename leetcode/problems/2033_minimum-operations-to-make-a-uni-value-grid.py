from typing import List


class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        rows, cols = len(grid), len(grid[0])

        # Flatten the grid and find the median value
        nums = [grid[r][c] for r in range(rows) for c in range(cols)]
        nums.sort()
        median = nums[len(nums) // 2]

        # Check if every number has the same remainder when divided by x
        # Also, calculate the number of operations required to make all numbers equal to the median
        ans = 0
        for num in nums:
            # Compute the difference between the number and the median
            diff = abs(num - median)

            # If the difference is not divisible by x, return -1
            if diff % x != 0:
                return -1

            # Otherwise, update answer by number of needed operations
            ans += diff // x

        return ans
