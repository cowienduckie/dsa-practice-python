from typing import List


class Solution:
    def check(self, nums: List[int]) -> bool:
        # Count number of pivots that the array decreases
        pivot = 0
        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                pivot += 1
        # The point between first and last could be a valid pivot itself
        if nums[0] < nums[-1]:
            pivot += 1
        # Sorted and rotated can only have 1 pivot at max
        return pivot < 2
