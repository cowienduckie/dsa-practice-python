from typing import List


class Solution:
    """
    Solution using binary search and line sweep
    """

    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        """
        Binary search for the leftmost valid k
        Time complexity: O(log(Q) * (N + Q))
        """

        # Check if we can have a zero array after all queries
        if not self._can_form_zero_array(nums, queries, len(queries)):
            return -1

        # Use binary search to find the smallest possible k
        l, r = 0, len(queries)
        while l <= r:
            k = l + (r - l) // 2
            if self._can_form_zero_array(nums, queries, k):
                r = k - 1
            else:
                l = k + 1

        return l

    def _can_form_zero_array(
        self, nums: List[int], queries: List[List[int]], k: int
    ) -> bool:
        """
        Check if array can be transformed to zero array with k first queries
        Time complexity: O(N + K) ~ O(N + Q)
        """

        n = len(nums)
        # Store a difference array of ranges
        diff = [0] * (n + 1)
        for i in range(k):
            # Extract left, right pointers, and diff value
            l, r, val = queries[i]
            # Update diff array
            diff[l] += val
            diff[r + 1] -= val

        # Traverse through both original and difference arrays
        # Try to decrease original number, if any number cannot reach at least 0, return False
        sub = 0
        for i in range(n):
            # Update subtrahend
            sub += diff[i]
            # Check if current number can reach 0
            if nums[i] > sub:
                return False

        return True


class Solution:
    """
    Solution using line sweep and single pass
    """

    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        n, q = len(nums), len(queries)
        # Store a difference array of ranges
        diff = [0] * (n + 1)
        # Traverse through all numbers and try to make each number reach 0 with minimum k queries
        sub = k = 0
        for i in range(n):
            while k <= q and nums[i] > sub + diff[i]:
                # Check if the total number of queries is exceeded
                if k == q:
                    return -1
                # Extract left, right pointers, and diff value
                l, r, val = queries[k]
                # If current range contains number i or i + x, update diff array
                if r >= i:
                    diff[max(l, i)] += val
                    diff[r + 1] -= val
                # Update k
                k += 1
            sub += diff[i]
        # Return the minimum needed queries
        return k
