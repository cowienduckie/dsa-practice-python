from typing import List


class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        max_num = max_diff = max_value = 0

        for num in nums:
            max_value = max(max_value, num * max_diff)
            max_diff = max(max_diff, max_num - num)
            max_num = max(max_num, num)

        return max_value
