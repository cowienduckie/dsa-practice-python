class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        ans = 0
        for num in range(1, n + 1):
            if num % m == 0:
                ans -= num
            else:
                ans += num
        return ans
