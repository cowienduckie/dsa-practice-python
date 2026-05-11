from typing import List


class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(len(nums) - 1, -1, -1):
            num = nums[i]
            while num:
                ans.append(num % 10)
                num //= 10
        return ans[::-1]
