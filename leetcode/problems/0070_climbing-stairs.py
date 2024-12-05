class Solution:
    def __init__(self):
        self.dp = [0] * 46
        self.dp[1] = 1
        self.dp[2] = 2

    def climbStairs(self, n: int) -> int:
        if n < 1:
            return 0
        if self.dp[n] == 0:
            self.dp[n] = self.climbStairs(n - 1) + self.climbStairs(n - 2)

        return self.dp[n]
