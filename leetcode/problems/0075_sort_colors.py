from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Count the frequency of 3 colors
        freq = [0] * 3
        for color in nums:
            freq[color] += 1
        # Fill the colors by quantity into the original array from 0 to 2
        for i in range(len(nums)):
            for color in range(3):
                if freq[color]:
                    nums[i] = color
                    freq[color] -= 1
                    break
