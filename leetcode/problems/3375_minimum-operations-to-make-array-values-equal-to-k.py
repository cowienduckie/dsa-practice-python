from typing import List


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        min_num = min(nums)
        if min_num < k:
            return -1
        distinct_cnt = len(set(nums))
        return distinct_cnt - 1 if min_num == k else distinct_cnt
