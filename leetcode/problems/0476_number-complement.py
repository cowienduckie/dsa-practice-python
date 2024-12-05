class Solution:
    def findComplement(self, num: int) -> int:
        ans = 0
        leading_zero = True

        for i in range(30, -1, -1):  # Loop backward from 30 to 0
            power = 2**i

            if leading_zero and num < power:
                continue
            else:
                leading_zero = False

            if num >= power:
                num = num - power
            else:
                ans = ans + power

        return ans
