from typing import List


class Solution:
    """
    Solution using Greedy

    Consider we have an array [x1, x2, ..., xn]
    1. If x1 = 0, then the only way x1 could become 1 is that flip [x1, x2, x3]
    2. If x1 = 1, then the problem is that flip [x2 .. xn] instead
    3. If the array is [x1, x2], the only way it could be [1, 1] is that it already [1, 1] from the beginning

    With 3 above statements, we can come up with a greedy solution that checking each number strictly from left to right
    And trying to flip them to 1 no matter how 2 next consecutive numbers could be.
    """

    def minOperations(self, nums: List[int]) -> int:
        ans = 0

        for i in range(len(nums) - 2):
            if not nums[i]:
                nums[i + 1] = 1 - nums[i + 1]
                nums[i + 2] = 1 - nums[i + 2]
                ans += 1

        return ans if nums[i + 1] and nums[i + 2] else -1
