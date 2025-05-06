class Solution:
    """
    Solution using DP and math

    A[n] is a fulfilled board of size n x 2
    B[n] is a fulfilled board of size (n + 1) x 2 except 1 cell at last column (there are 2 cases B1, B2 based on the last filled cell)

    To construct A[n], we have 3 options:
    1. A[n - 1] + 1 vertical domino
    2. A[n - 2] + 2 horizontal dominoes
    3. B[n - 2] + 1 tromino (2 cases)
    -> A[n] = A[n - 1] + A[n - 2] + 2 * B[n - 2]

    To construct B[n], we have 2 options:
    1. A[n - 1] + 1 tromino
    2. B[n - 1] + 1 horizontal domino
    -> B[n] = A[n - 1] + B[n - 1]
            = A[n - 1] + A[n - 2] + B[n - 2]
            = ...
            = sum(A[i] for i = 0 -> n - 1)

    -> A[n] = A[n - 1] + A[n - 2] + 2 * sum(A[i] for i = 0 -> n - 3)

    We also have:
    A[n - 1] = A[n - 2] + A[n - 3] + 2 * sum(A[i] for i = 0 -> n - 4)
             = A[n - 2] + 2 * sum(A[i] for i = 0 -> n - 3) - A[n - 3]
    -> A[n - 2] + 2 * sum(A[i] for i = 0 -> n - 3) = A[n - 1] + A[n - 3]

    In the end, we have:
    A[n] = 2 * A[n - 1] + A[n - 3]
    """

    def numTilings(self, n: int) -> int:
        if n < 3:
            return n
        MOD = 1_000_000_007
        dp = [1] * (n + 1)
        dp[2] = 2
        for i in range(3, n + 1):
            dp[i] = (2 * dp[i - 1] + dp[i - 3]) % MOD
        return dp[n]
