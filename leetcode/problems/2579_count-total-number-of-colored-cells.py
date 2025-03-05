class Solution:
    """
    Solution using math

    Check some cases with small n:
        n = 1 -> F(1) = 1
        n = 2 -> F(2) = 5
        n = 3 -> F(3) = 13
        n = 4 -> F(4) = 25

    We can see that
    F(n) = F(n - 1) + 4(n - 1)
         = 4[n - 1 + n - 2 + ... + n - (n - 1)] + F(1)
         = 4[(n - 1) * n - (n - 1) * n / 2] + 1
         = 2(n - 1)n + 1
    """

    def coloredCells(self, n: int) -> int:
        return 2 * n * (n - 1) + 1


class Solution:
    """
    Solution using recursion in case we can't see the pattern quickly
    """

    def coloredCells(self, n: int) -> int:
        if n == 1:
            return 1
        return self.coloredCells(n - 1) + 4 * (n - 1)
