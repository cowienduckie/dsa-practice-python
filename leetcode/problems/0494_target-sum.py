from typing import List, Optional


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = [
            [None] * (1000 * 2 + 1) for _ in range(len(nums))
        ]  # 0 <= sum(nums) <= 1000

        def traverse(pos: int, curr_sum: int) -> int:
            # Base case
            if pos == len(nums):
                return 1 if curr_sum == target else 0
            # If already calculated, return the value
            if memo[pos][curr_sum]:
                return memo[pos][curr_sum]
            # Try adding and subtracting the current number
            ans = 0
            ans += traverse(pos + 1, curr_sum + nums[pos])
            ans += traverse(pos + 1, curr_sum - nums[pos])
            # Save the result
            memo[pos][curr_sum] = ans
            return ans

        return traverse(0, 0)
