from collections import defaultdict
from typing import List


class Solution:
    def isGood(self, nums: List[int]) -> bool:
        n = len(nums) - 1
        cnt = defaultdict(int)
        for num in nums:
            cnt[num] += 1
            if num > n or (num == n and cnt[num] > 2) or (num < n and cnt[num] > 1):
                return False
        return True
