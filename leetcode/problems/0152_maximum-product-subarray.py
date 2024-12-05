from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = float("-inf")
        curr_max = 1
        curr_min = 1
        for num in nums:
            if num < 0:
                curr_max, curr_min = curr_min, curr_max
            curr_max = max(curr_max * num, num)
            curr_min = min(curr_min * num, num)
            ans = max(ans, curr_max)
        return ans
