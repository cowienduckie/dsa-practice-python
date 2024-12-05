from typing import List


class Solution:
    """
    Solution using dynamic programming with O(n) space complexity.
    Because the houses are arranged in a circle, we can split the problem into two sub-problems (same as 0198_house-robber):
        - Rob houses [1, n - 1]
        - Rob houses [0, n - 2]
    Base case is when n < 4, we only can rob one house, so we return the maximum value.
    """

    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 4:
            return max(nums)

        return max(self.linear_rob(nums[: n - 1]), self.linear_rob(nums[1:]))

    def linear_rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return max(nums)

        dp = [0] * n
        dp[n - 1] = nums[n - 1]
        dp[n - 2] = nums[n - 2]
        dp[n - 3] = max(nums[n - 2], nums[n - 3] + nums[n - 1])

        for i in range(n - 4, -1, -1):
            dp[i] = nums[i] + max(dp[i + 2], dp[i + 3])

        return max(dp[0], dp[1])


class Solution:
    """
    Optimize linear_rob method by using O(1) space complexity.
    """

    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 4:
            return max(nums)

        return max(self.linear_rob(nums[: n - 1]), self.linear_rob(nums[1:]))

    def linear_rob(self, nums: List[int]) -> int:
        curr_max = prev_max = 0
        for num in nums:
            curr_max, prev_max = max(curr_max, prev_max + num), curr_max

        return curr_max
