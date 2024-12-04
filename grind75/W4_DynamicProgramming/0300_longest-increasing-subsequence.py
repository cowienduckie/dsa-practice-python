from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n, ans = len(nums), 1
        dp = [1] * n

        for i in range(n - 2, -1, -1):
            for j in range(i + 1, n):
                if nums[i] < nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
            ans = max(ans, dp[i])

        return ans
