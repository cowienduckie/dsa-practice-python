from typing import List


class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)
        # Create 2D array to store every changes through queries of each index
        changes = [
            [value if l <= i <= r else 0 for l, r, value in queries] for i in range(n)
        ]
        # Iterate through original numbers and check if it can be transform into 0 though minimum k changes
        ans = 0
        for i in range(n):
            min_changes = self._minimum_changes(changes[i], nums[i])

            if min_changes == -1:
                return -1
            else:
                ans = max(ans, min_changes)

        return ans

    def _minimum_changes(self, changes: List[int], target: int) -> int:
        # If target already 0, no need to transform
        if target == 0:
            return 0
        # Store the all combination of changes, resulting smaller or equal than target
        can_combine = [False] * (target + 1)
        can_combine[0] = True
        for k, change in enumerate(changes):
            # Check all combination with k-th change from k-th query
            for num in range(target, -1, -1):
                if can_combine[num] and num + change <= target:
                    can_combine[num + change] = True
            # Early return if target reach
            if can_combine[target]:
                return k + 1
        # Return -1 if no combination equal target
        return -1
