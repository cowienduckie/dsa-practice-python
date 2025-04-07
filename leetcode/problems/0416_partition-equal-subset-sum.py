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


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # Compute the sum of the array
        arr_sum = sum(nums)

        # If the sum is odd, we cannot partition it into two equal subsets
        if arr_sum & 1:
            return False

        # Use a set to store the sums we can achieve
        possible_sums = {0}
        for num in nums:
            # For each number, compute the new sums we can achieve
            new_sums = {
                ps + num for ps in possible_sums if ps + num not in possible_sums
            }
            # Early exit if we can achieve half of the total sum
            if arr_sum // 2 in new_sums:
                return True
            # Update the set of possible sums
            possible_sums.update(new_sums)
        return False


print(Solution().canPartition([1, 2, 5]))
