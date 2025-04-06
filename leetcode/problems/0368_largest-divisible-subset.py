from typing import List


class Solution:
    """
    Solution using memoization to find the largest divisible subset.

    Assume we have a sorted list of numbers, and given index i > j > k
    If nums[i] % nums[j] == 0 and nums[j] % nums[k] == 0
    Then nums[i] % nums[k] == 0

    So we can use memoization to store the longest divisible subset
    """

    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        # Sort the input list
        n = len(nums)
        nums.sort()

        # Use array to store the longest divisible subset as longest prefix numbers
        prefix = [None] * n
        ans = []

        # Iterate through the sorted list
        # For each number, check all previous numbers and update answer if we find a longer subset
        for i in range(n):
            longest_prefix = []
            j = 0
            # Check all possible previous divisors
            while nums[j] <= nums[i] // 2:
                if nums[i] % nums[j] == 0 and len(longest_prefix) < len(prefix[j]):
                    longest_prefix = prefix[j]
                j += 1

            # Update the prefix subset for the current number
            prefix[i] = longest_prefix + [nums[i]]

            # Update final answer if we find a longer subset
            if len(ans) < len(prefix[i]):
                ans = prefix[i]
        return ans
