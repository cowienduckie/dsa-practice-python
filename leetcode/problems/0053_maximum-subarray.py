from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Iterate the array and calculate prefix sum of all elements ending at position i
        # At position i, if nums[i] > sum[i - 1] + nums[i] then take only nums[i] in new sub-array
        n = len(nums)
        max_sum = nums[0]
        current_sum = nums[0]

        for i in range(1, n):
            current_sum = max(current_sum + nums[i], nums[i])
            max_sum = max(max_sum, current_sum)

        return max_sum
