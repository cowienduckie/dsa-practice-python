from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []

        def make_subsets(pos: int, curr_set: List[int]) -> None:
            if pos == n:
                nonlocal ans
                ans.append(curr_set)
                return

            make_subsets(pos + 1, curr_set)
            make_subsets(pos + 1, curr_set + [nums[pos]])

        make_subsets(0, [])
        return ans
