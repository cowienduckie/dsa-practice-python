from typing import List


class Solution:
    def maxSum(self, nums: List[int]) -> int:
        distinct_positive = set([num for num in nums if num > 0])
        max_num = max(nums)

        return sum(distinct_positive) if distinct_positive else max_num
