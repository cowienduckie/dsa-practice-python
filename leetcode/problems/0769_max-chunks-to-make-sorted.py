from typing import List


class Solution:
    """
    Solution using greedy and 2 pointers to check each chunk is valid
    The target permutation is always [0, 1, ..., n-1]
    So a valid chunk [i, j] must be followed these condition:
        - The minimum number must be i
        - The maximum number must be j
        - Length of chunk must be j - i
    """

    def maxChunksToSorted(self, arr: List[int]) -> int:
        # Track left, right pointers and max, min values of each chunk
        curr_min, curr_max = float("inf"), float("-inf")
        ans = l = 0
        for r in range(len(arr)):
            curr_min = min(curr_min, arr[r])
            curr_max = max(curr_max, arr[r])
            # If we found a valid chunk, update answer and start a new chunk
            if r == curr_max and l == curr_min:
                ans = ans + 1
                l = r + 1
                curr_min, curr_max = float("inf"), float("-inf")

        return ans
