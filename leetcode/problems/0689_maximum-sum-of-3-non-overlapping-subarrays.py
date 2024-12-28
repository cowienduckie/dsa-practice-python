from typing import List


class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        # Calculate the sum of each subarray of length k
        sub = [0] * n
        sub[k - 1] = sum(nums[0:k])
        for i in range(k, n):
            sub[i] = sub[i - 1] + nums[i] - nums[i - k]

        # dp1[i] is the index of the maximum sum subarray of length k ending at i
        dp1 = [None] * n
        dp1[k - 1] = k - 1
        for i in range(k, n):
            dp1[i] = i if sub[i] > sub[dp1[i - 1]] else dp1[i - 1]

        # dp2[i] is the indices of the maximum sum subarray of length 2k ending at i
        dp2 = [None] * n
        dp2[2 * k - 1] = (k - 1, 2 * k - 1)
        for i in range(2 * k, n):
            if sub[i] + sub[dp1[i - k]] > sub[dp2[i - 1][0]] + sub[dp2[i - 1][1]]:
                dp2[i] = (dp1[i - k], i)
            else:
                dp2[i] = dp2[i - 1]

        # dp3[i] is the indices of the maximum sum subarray of length 3k ending at i
        dp3 = [None] * n
        dp3[3 * k - 1] = (k - 1, 2 * k - 1, 3 * k - 1)
        for i in range(3 * k, n):
            if (
                sub[i] + sub[dp2[i - k][0]] + sub[dp2[i - k][1]]
                > sub[dp3[i - 1][0]] + sub[dp3[i - 1][1]] + sub[dp3[i - 1][2]]
            ):
                dp3[i] = (dp2[i - k][0], dp2[i - k][1], i)
            else:
                dp3[i] = dp3[i - 1]

        return [i - k + 1 for i in dp3[n - 1]]
