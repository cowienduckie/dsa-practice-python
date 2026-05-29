from ast import List


class Solution:
    def minElement(self, nums: List[int]) -> int:
        ans = float("inf")
        for num in nums:
            ans = min(ans, self._digit_sum(num))
        return ans

    def _digit_sum(self, num: int) -> int:
        s = 0
        while num:
            s += num % 10
            num //= 10
        return s
