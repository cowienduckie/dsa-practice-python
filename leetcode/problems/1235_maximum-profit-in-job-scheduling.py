from bisect import bisect_right
from typing import List


class Solution:
    def jobScheduling(
        self, startTime: List[int], endTime: List[int], profit: List[int]
    ) -> int:
        n = len(profit)
        # Sort all jobs by end time, create a indices array to convert new endTime index to old one
        indices = sorted(range(n), key=lambda i: endTime[i])
        endTime.sort()

        # Use an array to store the optimal profit by ending of job i-th
        dp = [0] * n
        for i in range(n):
            # If we do not take job i-th, we have the same profit as the previous one
            not_take = dp[i - 1]

            # If we take job i-th, we need to find the latest job ending before job i-th
            prev = bisect_right(endTime, startTime[indices[i]])
            take = profit[indices[i]] + (dp[prev - 1] if prev > 0 else 0)

            # Consider wether we should take job i-th or not
            dp[i] = max(take, not_take)

        return dp[n - 1]
