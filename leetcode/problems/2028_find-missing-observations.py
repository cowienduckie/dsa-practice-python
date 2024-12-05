from typing import List


class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        # Calculate sum of n rolls
        m = len(rolls)
        sum_m = sum(rolls)
        sum_n = mean * (n + m) - sum_m

        # Try to generate an array have sum equal to sum_n
        # If mean of n rolls is out of bound -> return empty
        # Otherwise, we spread floor of mean of n rolls in the array, then fill the leftover
        mean_n = sum_n * 1.0 / n
        ans = []

        if mean_n >= 1 and mean_n <= 6:
            mean_n = sum_n // n
            sum_n -= mean_n * n

            ans = [mean_n] * n
            i = 0

            while sum_n > 0:
                if 6 - ans[i] < sum_n:
                    sum_n -= 6 - ans[i]
                    ans[i] = 6
                else:
                    ans[i] += sum_n
                    sum_n = 0
                i += 1

        return ans


print(Solution().missingRolls([1, 5, 6], 3, 4))  # [2, 3, 2, 2]
