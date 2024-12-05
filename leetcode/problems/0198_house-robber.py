from typing import List


class Solution:
    """
    Solution using dynamic programming with O(n) space complexity.
    """

    def rob(self, nums: List[int]) -> int:
        dp = [0]

        for i, n in enumerate(nums, start=1):
            if i <= 2:
                dp.append(n)
                continue
            dp.append(n + max(dp[i - 2], dp[i - 3]))

        return max(dp)


class Solution:
    """
    Solution using dynamic programming with O(1) space complexity.
    """

    def rob(self, nums: List[int]) -> int:
        curr_max = prev_max = 0

        for num in nums:
            curr_max, prev_max = max(curr_max, prev_max + num), curr_max

        return curr_max
