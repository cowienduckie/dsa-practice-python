from typing import List


class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        prev = -1
        for i, num in enumerate(nums):
            if num == 0:
                continue
            if prev != -1 and i - prev - 1 < k:
                return False
            prev = i
        return True
