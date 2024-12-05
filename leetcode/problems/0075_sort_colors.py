from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # red = 0, white = 1, blue = 2
        red, white = 0, 0

        for num in nums:
            if num == 0:
                red = red + 1
            elif num == 1:
                white = white + 1

        for i in range(red):
            nums[i] = 0
        for i in range(red, red + white):
            nums[i] = 1
        for i in range(red + white, len(nums)):
            nums[i] = 2
