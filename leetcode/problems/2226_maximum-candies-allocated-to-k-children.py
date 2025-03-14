from typing import List


class Solution:
    """
    Solution using binary search
    Time complexity: O(n * log(m))
    """

    def maximumCandies(self, candies: List[int], k: int) -> int:
        total_candies = sum(candies)

        # Return 0 if there is not enough candies to distribute 1 candy for each kid
        if total_candies < k:
            return 0

        # Use binary search to find the maximum candies can distribute for each kid
        left, right = 1, total_candies // k
        while left <= right:
            mid = left + (right - left) // 2
            # Try to increase the distributed candies
            if self._can_distribute(candies, k, mid):
                left = mid + 1
            else:
                right = mid - 1

        return right

    def _can_distribute(self, candies: List[int], k: int, x: int) -> bool:
        # Try to distribute x candies for each kid
        for c in candies:
            k = k - c // x
            if k <= 0:
                return True
        return False
