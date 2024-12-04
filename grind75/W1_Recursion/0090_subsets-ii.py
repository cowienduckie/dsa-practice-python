from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        ans = []

        def make_subsets(pos: int, curr_set: List[int]) -> None:
            if pos == n:
                nonlocal ans
                ans.append(curr_set)
                return

            # Find the index of the next different number
            next_diff = pos + 1
            while next_diff < n and nums[next_diff] == nums[pos]:
                next_diff += 1

            # For each num[pos] subset size, add the current number that many times to the current subset
            # Then jump to the next different number
            for i in range(pos, next_diff):
                make_subsets(next_diff, curr_set + [nums[pos]] * (i - pos))

        make_subsets(0, [])
        return ans
