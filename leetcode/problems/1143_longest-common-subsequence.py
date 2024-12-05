class Solution:
    """
    Dynamic Programming
    Time complexity: O(n1 * n2)
    """

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """
        Given N1 and N2 as the lengths of text1 and text2, respectively.

        Use a N1 x N2 matrix to store the length of the longest common subsequence (LCS).
        We could see that LCS ending at text1[i] and text2[j] have two cases:
            - text1[i] == text2[j]: LCS(i, j) = LCS(i - 1, j - 1) + 1
            - text1[i] != text2[j]: LCS(i, j) = max(LCS(i - 1, j), LCS(i, j - 1))

        So, a cell (i, j) is determined by the cell (i - 1, j - 1), (i - 1, j), and (i, j - 1).
        We can pre-fill the top-left corner, top side, and left side of the matrix.
        Then build the matrix from the top-left corner to the bottom-right corner

        The answer is the value of the bottom-right corner of the matrix.
        """
        n1, n2 = len(text1), len(text2)
        dp = [[0] * n2 for _ in range(n1)]

        # Fill the top-left corner first
        if text1[0] == text2[0]:
            dp[0][0] = 1

        # Fill the top side
        for i in range(1, n1):
            dp[i][0] = 1 if text1[i] == text2[0] else dp[i - 1][0]

        # Fill the left side
        for j in range(1, n2):
            dp[0][j] = 1 if text1[0] == text2[j] else dp[0][j - 1]

        # Build the matrix from the top-left corner to the bottom-right corner
        for i in range(1, n1):
            for j in range(1, n2):
                if text1[i] == text2[j]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return dp[n1 - 1][n2 - 1]


class Solution:
    """
    Dynamic Programming with 2D array (Cleaner version)
    Instead of pre-filling the edges, we could create a 0-column and 0-row to the left and top of the matrix.
    """

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n1, n2 = len(text1), len(text2)
        dp = [[0] * (n2 + 1) for _ in range(n1 + 1)]

        # Build the matrix from the top-left corner to the bottom-right corner
        for i in range(1, n1 + 1):
            for j in range(1, n2 + 1):
                dp[i][j] = (
                    dp[i - 1][j - 1] + 1
                    if text1[i - 1] == text2[j - 1]
                    else max(dp[i - 1][j], dp[i][j - 1])
                )

        return dp[n1][n2]


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """
        Dynamic Programming with 1D array (Space-optimized version)
        """

        n1, n2 = len(text1), len(text2)
        dp = [0] * (n2 + 1)

        for i in range(1, n1 + 1):
            prev = 0
            for j in range(1, n2 + 1):
                temp = dp[j]
                if text1[i - 1] == text2[j - 1]:
                    dp[j] = prev + 1
                else:
                    dp[j] = max(dp[j], dp[j - 1])
                prev = temp

        return dp[n2]
