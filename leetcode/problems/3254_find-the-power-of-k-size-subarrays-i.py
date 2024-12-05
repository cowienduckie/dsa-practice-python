from collections import deque
from typing import List


class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        """
        Maintain a window of maximum size k.
            - If the pushing element is not consecutively increasing, clear the window.
            - If the window size reaches k, store the last element of the window.
        """
        n = len(nums)
        ans = []
        window = deque()

        for i in range(n):
            # If current element is not consecutively greater than the last element, clear the window.
            if window and nums[i] != window[-1] + 1:
                window.clear()
            window.append(nums[i])

            # Start storing the last element of the window when the window size is possible to reach k.
            if i >= k - 1:
                if len(window) == k:
                    ans.append(window[-1])
                    window.popleft()
                else:
                    ans.append(-1)
        return ans
