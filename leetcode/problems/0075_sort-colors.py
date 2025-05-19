from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        l, r = 0, n - 1

        for num in nums:
            if num % 10 == 0:
                nums[l] += 100
                l += 1
            elif num % 10 == 2:
                nums[r] += 1000
                r -= 1

        for i in range(n):
            if nums[i] < 100:
                nums[i] = 1
            elif nums[i] >= 1000:
                nums[i] = 2
            else:
                nums[i] = 0


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
