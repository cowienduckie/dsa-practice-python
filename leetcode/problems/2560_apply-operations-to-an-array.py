from typing import List


class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = []

        for i in range(n - 1):
            if nums[i] == 0:
                continue
            elif nums[i] == nums[i + 1]:
                ans.append(nums[i] * 2)
                nums[i + 1] = 0
            else:
                ans.append(nums[i])

        return ans + [nums[-1]] + [0] * (n - len(ans) - 1)
