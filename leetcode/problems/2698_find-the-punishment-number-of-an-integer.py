from cmath import log10


class Solution:
    def punishmentNumber(self, n: int) -> int:
        ans = 0
        for i in range(1, n + 1):
            if self.is_punishment(i * i, i):
                ans += i * i
        return ans

    def is_punishment(self, num: int, target: int) -> bool:
        # If the number cannot divide anymore, check the target reach 0 yet
        if num == 0:
            return target == 0
        # Early return false if the cannot make the target 0
        if target < 0 or target > num:
            return False
        # Try to divide the number by powers of 10
        for i in range(1, int(log10(num)) + 2):
            divider = 10**i
            # Early return if we have a correct way to divide the number
            if self.is_punishment(num // divider, target - (num % divider)):
                return True
        return False
