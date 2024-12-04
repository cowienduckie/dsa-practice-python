class Solution:
    def __init__(self):
        self.digits = {
            "0": 0,
            "1": 1,
            "2": 2,
            "3": 3,
            "4": 4,
            "5": 5,
            "6": 6,
            "7": 7,
            "8": 8,
            "9": 9,
        }

        self.signs = {"+", "-"}

    def myAtoi(self, s: str) -> int:
        reading = []
        sign = 1
        for char in s:
            # If not in reading mode, spaces and signs are allowed
            if not reading:
                if char == " ":
                    continue
                elif char in self.signs:
                    sign = 1 if char == "+" else -1
                    reading.append("0")
                elif char in self.digits:
                    reading.append(char)
                else:
                    break
            # If in reading mode, only digits are allowed
            else:
                if char in self.digits:
                    reading.append(char)
                else:
                    break

        if not reading:
            return 0

        s = self.remove_leading_zeros("".join(reading))

        return self.to_int(s[::-1], sign)

    def remove_leading_zeros(self, s: str) -> str:
        for i, char in enumerate(s):
            if char != "0":
                return s[i:]
        return "0"

    def to_int(self, s: str, sign: int) -> int:
        num = 0
        for i, char in enumerate(s):
            num += self.digits[char] * 10**i * sign
            if num > 2**31 - 1:
                return 2**31 - 1
            elif num < -(2**31):
                return -(2**31)
        return num
