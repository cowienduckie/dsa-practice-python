from typing import List


class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        n = len(nums)

        # Find the dominant element
        dominant = freq = 0
        for num in nums:
            if freq == 0:
                dominant = num
                freq = 1
            else:
                freq += 1 if num == dominant else -1

        # Count the total number of dominant elements
        dominant_total = 0
        for num in nums:
            if num == dominant:
                dominant_total += 1

        # Find the minimum index that can split the array
        dominant_count = 0
        for i in range(n):
            # Update the current count of dominant elements
            if nums[i] == dominant:
                dominant_count += 1

            # Check if the current index is a valid split
            if (
                dominant_count > (i + 1) // 2
                and dominant_total - dominant_count > (n - i - 1) // 2
            ):
                return i

        # If no valid split is found, return -1
        return -1


print(Solution().minimumIndex([1, 2, 2, 2]))
