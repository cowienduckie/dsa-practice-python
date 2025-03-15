from typing import List


class Solution:
    """
    Solution using binary search

    Q:  In this solution, why we don't have to care about the mid_cap not exists in nums?
    A:  Determine mid_cap is X, if the robber can steal with X cap, there is definitely number Y, which is Y < X and Y in nums.
        And the binary search will find Y later after moving the pointers.
    """

    def minCapability(self, nums: List[int], k: int) -> int:
        # Find the initial range of capability
        min_cap, max_cap = min(nums), max(nums)

        # Binary search for the minimum capability
        while min_cap <= max_cap:
            mid_cap = min_cap + (max_cap - min_cap) // 2

            # If robber can steal within mid_cap, try to decrease the max_cap
            if self._can_steal(nums, k, mid_cap):
                max_cap = mid_cap - 1
            else:
                min_cap = mid_cap + 1

        # Return the found minimum capability
        return min_cap

    def _can_steal(self, nums: List[int], k: int, cap: int) -> bool:
        i = 0
        while i < len(nums):
            # Check if robber can steal from i-th house
            if nums[i] <= cap:
                # Early return when meet at least k houses with money not exceed capability
                if k == 1:
                    return True
                # Skip the next house if current house is robbed
                else:
                    k = k - 1
                    i = i + 2
            else:
                i = i + 1
        return False
