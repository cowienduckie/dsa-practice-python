from bisect import bisect_left, bisect_right
from typing import List


class Solution:
    """
    Solution using built-in bisect functions
    """

    def maximumCount(self, nums: List[int]) -> int:
        # Use binary search to find the leftmost and rightmost index of 0
        leftmost_index = bisect_left(nums, 0)
        rightmost_index = bisect_right(nums, 0)

        # Return the max number of positive and negative numbers
        return max(leftmost_index, len(nums) - rightmost_index)


class Solution:
    """
    Solution using self-implemented binary search
    """

    def maximumCount(self, nums: List[int]) -> int:
        # Use binary search to find the leftmost and rightmost index of 0
        leftmost_index = self._binary_search_leftmost(nums, 0)
        rightmost_index = self._binary_search_rightmost(nums, 0)

        # Return the max number of positive and negative numbers
        return max(leftmost_index, len(nums) - rightmost_index)

    def _binary_search_rightmost(self, nums: List[int], target) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1

        return left

    def _binary_search_leftmost(self, nums: List[int], target) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return left
