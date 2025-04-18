class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        ans = 0
        for num in range(low, high + 1):
            if self._is_symmetric(num):
                ans += 1
        return ans

    def _is_symmetric(self, num: int) -> bool:
        digits = [int(d) for d in str(num)]
        if len(digits) & 1:
            return False
        return sum(digits[: len(digits) // 2]) - sum(digits[len(digits) // 2 :]) == 0
