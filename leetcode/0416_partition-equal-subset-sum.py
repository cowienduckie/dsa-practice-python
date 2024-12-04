from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        arr_sum = sum(nums)
        if arr_sum & 1:
            return False

        """
        The dp array stores the total obtained sums we have come across so far.
        Notice that dp[0] = True; if we never select any element, the total sum is 0.
        """
        dp = [True] + [False] * arr_sum
        for num in nums:
            for curr in range(arr_sum, num - 1, -1):
                """
                Case 1: The current sum (curr) has been seen before.
                        Then, if we don't select the current element, the sum will not change.
                        So, this total sum will still exist, and its dp value remains True.

                Case 2: The current sum (curr) has not been seen before,
                        but it can be obtained by selecting the current element.
                        This means that dp[curr-num] = True, and thus dp[curr] now becomes True.

                Case 3: The current sum (curr) has not been seen before,
                        and it cannot be obtained by selecting the current element.
                        So, this total sum will still not exist, and its dp value remains False.
                """
                dp[curr] = dp[curr - num] or dp[curr]

        return dp[arr_sum // 2]


class Solution2:
    """
    Optimized version using set and try to add the current element to all the sums we have seen so far.
    """

    def canPartition(self, nums: List[int]) -> bool:
        arr_sum = sum(nums)
        if arr_sum & 1:
            return False

        dp = set([0])
        for num in nums:
            dp |= {num + x for x in dp}

        return arr_sum // 2 in dp


print(Solution().canPartition([1, 2, 5]))
