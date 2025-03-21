from typing import List


class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        banned_set = set(banned)
        ans = 0
        for num in range(1, n + 1):
            if num in banned_set:
                continue
            if maxSum < num:
                break
            maxSum -= num
            ans += 1
        return ans
