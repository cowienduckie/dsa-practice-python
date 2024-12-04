from typing import List


class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        # Find the longest valid right sub-array and remove all the left sub-array
        n = len(arr)
        r = n - 1
        while r > 0 and arr[r] >= arr[r - 1]:
            r = r - 1

        # Expand the left sub-array and remove middle sub-array, update the longest middle
        # Once the right pointer move out from array, we have the case that keep left part and remove right part
        ans = r
        l = 0
        arr.append(float("-inf"))
        while l < r and arr[l] >= arr[l - 1]:
            while r < n and arr[l] > arr[r]:
                r = r + 1
            ans = min(ans, r - l - 1)
            l = l + 1
        return ans
