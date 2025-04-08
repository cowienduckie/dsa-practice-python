from typing import List


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        existed = set()
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] in existed:
                return i // 3 + 1
            else:
                existed.add(nums[i])
        return 0
