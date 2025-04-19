from bisect import bisect_left, bisect_right
from typing import List


class Solution:
    """
    Solution using built-in bisect functions
    """

    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        n = len(nums)

        # Sort the array because we actually no need to consider the order of indices
        nums.sort()

        # For each index i, find the leftmost and rightmost values of index j
        # Number of fair pairs is equal to number of indices j found
        ans = 0
        for i in range(n - 1):
            l = bisect_left(nums, lower - nums[i], i + 1, n)
            r = bisect_right(nums, upper - nums[i], i + 1, n)
            ans += r - l
        return ans


class Solution:
    """
    Solution using self-implemented binary search
    """

    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        n = len(nums)

        # Sort the array because we actually no need to consider the order of indices
        nums.sort()

        # Binary search for the leftmost value
        def binary_search_left(target, left, right):
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return left

        # For each index i, find the leftmost and rightmost values of index j
        # Number of fair pairs is equal to number of indices j found
        ans = 0
        for i in range(n - 1):
            # Compute lower and upper bounds of index j
            lo = lower - nums[i]
            hi = upper - nums[i]

            # Find the leftmost value of index j
            leftmost = binary_search_left(lo, i + 1, n - 1)

            # Find the rightmost value of index j
            # A trick here is that we can add 1 to the upper-bound, so the leftmost of (hi + 1) is the rightmost of hi
            rightmost = binary_search_left(hi + 1, i + 1, n - 1)

            # Count the number of indices j found
            ans += rightmost - leftmost
        return ans
