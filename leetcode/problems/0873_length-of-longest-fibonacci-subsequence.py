from typing import List


class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        n = len(arr)
        # Use a 2D array to store longest Fibonacci subseq ending with arr[j] and arr[k] as dp[j][k], j < k
        dp = [[2] * n for _ in range(n)]
        ans = 0

        for k in range(2, n):
            # Use 2 pointers to find pairs (i, j) that arr[i] + arr[j] == arr[k]
            i, j = 0, k - 1
            while i < j:
                if arr[i] + arr[j] > arr[k]:
                    j -= 1
                elif arr[i] + arr[j] < arr[k]:
                    i += 1
                else:
                    dp[j][k] = max(dp[j][k], dp[i][j] + 1)
                    ans = max(ans, dp[j][k])
                    i += 1
                    j -= 1

        return ans
