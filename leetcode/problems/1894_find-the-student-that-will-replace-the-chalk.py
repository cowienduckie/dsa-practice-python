from typing import List


class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        # Loop through the array and memoize total of chalk usage from 0 to i students
        n = len(chalk)
        chalk_usage: List[int] = list(chalk)

        for i in range(1, n):
            chalk_usage[i] += chalk_usage[i - 1]

        # Calculate k modulo chalk_usage[-1] to get the last round
        # Then check at which position use more than the residual
        k = k % chalk_usage[-1]
        for i in range(n):
            if chalk_usage[i] > k:
                return i

        return -1
