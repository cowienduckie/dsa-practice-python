class Solution:
    """
    DP solution using memoized 3D-array

    Time complexity: O(m * n * k)
    Space complexity: O(m * n * k)
    """
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        MOD = 1_000_000_007
        rows, cols = len(grid), len(grid[0])
        
        # Initialize DP 3D-array to store all remainders modulo k of all sums ended at each cell
        dp = [[[0] * k for _ in range(cols)] for _ in range(rows)]
        dp[0][0][grid[0][0] % k] = 1

        # Traverse from top-left to bottom-right
        for r in range(rows):
            for c in range(cols):
                for old_rem in range(k):
                    # Calculate new remainder
                    new_rem = (old_rem + grid[r][c]) % k
                    # Update current cell's remainders array
                    if r > 0:
                        dp[r][c][new_rem] += dp[r - 1][c][old_rem]
                    if c > 0:
                        dp[r][c][new_rem] += dp[r][c - 1][old_rem]
                    dp[r][c][new_rem] %= MOD

        # Return number of sums ended at most bottom-right cell that are divisible by k           
        return dp[rows - 1][cols - 1][0]
