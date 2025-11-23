from typing import List


class TwoSmallest:
    """
    Helper class to track the two smallest numbers of a certain category.
    """

    def __init__(self):
        self.smallest = None
        self.second_smallest = None

    def update(self, num: int) -> None:
        """Update the two smallest numbers with a new number."""
        # Case 1: smallest is not set
        if not self.smallest:
            self.smallest = num
        # Case 2: only smallest is set
        # Case 3: both smallest and second_smallest are set and num is smaller than second smallest
        elif not self.second_smallest or num <= self.second_smallest:
            self.smallest, self.second_smallest = min(self.smallest, num), max(
                self.smallest, num
            )

    def get_sum(self) -> int:
        """Get the sum of the two smallest numbers."""
        return (
            self.smallest + self.second_smallest
            if self.second_smallest
            else float("inf")
        )

    def get_smallest(self) -> int:
        """Get the smallest number."""
        return self.smallest if self.smallest else float("inf")


class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        # Initialize total sum and 2 smallest trackers for mod 1 and mod 2 numbers
        ans = 0
        mod_1 = TwoSmallest()
        mod_2 = TwoSmallest()
        # Iterate through numbers to calculate total sum and track smallest mod 1 and mod 2 numbers
        for num in nums:
            ans += num
            if num % 3 == 1:
                mod_1.update(num)
            elif num % 3 == 2:
                mod_2.update(num)
        # Adjust total sum to be divisible by 3 if necessary
        if ans % 3 == 1:
            ans -= min(mod_1.get_smallest(), mod_2.get_sum())
        elif ans % 3 == 2:
            ans -= min(mod_2.get_smallest(), mod_1.get_sum())
        return ans
