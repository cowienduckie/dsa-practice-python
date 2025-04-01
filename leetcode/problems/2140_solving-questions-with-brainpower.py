from typing import List


class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        # Use DP array to store the best points could get when starting at index i
        n = len(questions)
        dp = [0] * n
        dp[n - 1] = questions[n - 1][0]

        for i in range(n - 2, -1, -1):
            # Extract the question i points and brainpowers
            pts, skip = questions[i]

            # Compare the points when picking question i or not
            if i + skip + 1 < n:
                dp[i] = max(pts + dp[i + skip + 1], dp[i + 1])
            else:
                dp[i] = max(pts, dp[i + 1])

        # Return the maximum points could get from index 0
        return dp[0]
