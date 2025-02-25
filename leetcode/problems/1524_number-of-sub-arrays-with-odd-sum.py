from typing import List


class Solution:
    """
    Solution using prefix sum - O(n^2) time complexity

    First thought: The sum of an array is odd if and only if it has odd number of odd elements
    So, we can solve this problem by:
        1. Count the number of odd elements before each index
        2. Use 2 loops to check every subarray by above prefix count
    """

    def numOfSubarrays(self, arr: List[int]) -> int:
        n = len(arr)

        # Count number of odd before each indices
        prefix = [0] * (n + 1)

        for i in range(1, n + 1):
            prefix[i] = prefix[i - 1] + (1 if arr[i - 1] & 1 else 0)

        # Use 2 loop to check every subarray
        MOD = 1000000007
        ans = 0
        prev = 0

        for i in range(1, n + 1):
            if prefix[i] == prefix[i - 1]:
                ans = (ans + prev) % MOD
            else:
                prev = i - prev
                ans = (ans + prev) % MOD

        return ans


class Solution:
    """
    Optimized solution using DP - O(n) time complexity

    First thought: Look into logic of the above solution, there are 2 cases when adding arr[i]:
        1. If arr[i] is even, the final answer increase by exactly same as when adding arr[i - 1]
        2. If arr[i] is odd, all subarrays ending at arr[i - 1] with even sum now have odd sum, and vice versa

    Follow the above logic, we can construct a dynamic programming solution
    by imagining the prefix sum but not actually implement it
    """

    def numOfSubarrays(self, arr: List[int]) -> int:
        MOD = 1000000007
        ans = prev = 0

        for i in range(len(arr)):
            if arr[i] & 1:
                prev = i - prev + 1
            ans = (ans + prev) % MOD

        return ans
