from typing import List


class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        low = 0
        high = nums[-1] - nums[0]

        while low < high:
            mid = (high + low) // 2

            if self.count_pairs(nums, mid) < k:
                low = mid + 1
            else:
                high = mid

        return low

    def count_pairs(self, nums: List[int], distance: int) -> int:
        count = left = 0

        for right in range(1, len(nums)):
            while (nums[right] - nums[left] > distance):
                left += 1
            count += right - left

        return count
