from typing import List


class Solution:
    """
    Solution using two pointers

    Given a diff array, there are only (upper - lower) = X hidden arrays.
    Because after choosing a fixed number at one index, the rest of array could be constructed.
    So, we assume that the index 0 have X choices, iterate through the rest of diff array and track that amount of choices remained.
    """

    def numberOfArrays(self, diff: List[int], lower: int, upper: int) -> int:
        # Use 2 pointers to maintain range [lo, hi] of choices at index i
        lo, hi = lower, upper
        for i in range(len(diff)):
            # Update the range but not exceed the given boundaries
            lo = max(lo + diff[i], lower)
            hi = min(hi + diff[i], upper)
            # Early return if there is not any choice
            if hi < lo:
                return 0
        # Return number of remaining choices
        return hi - lo + 1
