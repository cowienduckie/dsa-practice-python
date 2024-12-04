from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ans = [0] * n
        stack = []

        for i in range(n - 1, -1, -1):
            t = temperatures[i]
            while stack:
                last, j = stack[-1]
                if t < last:
                    ans[i] = j - i
                    break
                stack.pop()
            stack.append((t, i))

        return ans
