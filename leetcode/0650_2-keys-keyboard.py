from math import floor, sqrt
from typing import Dict


class Solution:
    dp: Dict[int, int] = {1: 0, 2: 2}

    def minSteps(self, n: int) -> int:
        if n in self.dp:
            return self.dp[n]

        # If n is not a prime number, find the minimum factor i
        # then, find the minimum steps of n / i
        # finally, copy it and paste (i - 1) times
        for i in range(2, floor(sqrt(n) + 1)):
            if n % i == 0:
                self.dp[n] = self.minSteps(n // i) + i
                return self.dp[n]

        # If n is a prime number, the minimum steps is itself
        self.dp[n] = n
        return self.dp[n]
