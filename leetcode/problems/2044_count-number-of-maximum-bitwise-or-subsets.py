from typing import List


class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        n = len(nums)
        max_or = 0

        for num in nums:
            max_or = max(max_or, max_or | num)

        def count_subset(pos: int, curr_or: int) -> int:
            if pos == n:
                return 1 if curr_or == max_or else 0

            return count_subset(pos + 1, curr_or) + count_subset(
                pos + 1, curr_or | nums[pos]
            )

        return count_subset(0, 0)
