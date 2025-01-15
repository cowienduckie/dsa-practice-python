class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        cnt1 = self.count_set_bits(num1)
        cnt2 = self.count_set_bits(num2)

        # If num2 has more 1-bits than num1, we need to fill the smallest 0-bits
        if cnt2 > cnt1:
            diff = cnt2 - cnt1
            for i in range(31):
                if not num1 & (1 << i):
                    num1 |= 1 << i
                    diff -= 1
                if diff == 0:
                    return num1
            return num1
        # If num2 has less 1-bits than num1, we need to toggle the greatest 1-bits
        elif cnt2 < cnt1:
            ans = 0
            for i in range(30, -1, -1):
                if num1 & (1 << i):
                    ans ^= 1 << i
                    cnt2 -= 1
                if cnt2 == 0:
                    return ans
            return ans
        # Otherwise, the answer is num1 itself
        else:
            return num1

    def count_set_bits(self, num: int) -> int:
        cnt = 0
        for i in range(31):
            if num & (1 << i):
                cnt += 1
        return cnt


print(Solution().minimizeXor(25, 72))  # 24
