from typing import List


class Solution:
    """
    Solution using dynamic programming by 1D array.
    At each index i-th, the best score is the maximum of the following two:
        - Take the previous best pair and replace the previous value with the current value.
        - Create a new pair with the current value and the previous value.
    """

    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        n, ans = len(values), 0
        dp = [0] * n

        for i in range(1, n):
            dp[i] = max(
                dp[i - 1] - values[i - 1] + values[i] - 1, values[i - 1] + values[i] - 1
            )
            ans = max(ans, dp[i])

        return ans


class Solution:
    """
    Optimized version using a single variable to store the previous best score.
    """

    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        ans, prev = 0, values[0]

        for i in range(1, len(values)):
            ans = max(ans, prev + values[i] - i)
            prev = max(prev, values[i] + i)

        return ans
