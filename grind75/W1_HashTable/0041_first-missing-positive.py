from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        nums.append(0)  # Add a dummy number to make sure index n could be swap

        for i in range(n):
            # If nums[i] is a possible answer and no duplicator before
            # Then swap until nums[i] is no more possible
            while 0 < nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]

        # Find the first missing positive number
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1

        return n + 1
