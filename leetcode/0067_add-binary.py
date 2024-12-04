class Solution:
    """
    One-liner solution.
    """

    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a, 2) + int(b, 2))[2:]


class Solution:
    """
    String manipulation solution.
    """

    def addBinary(self, a: str, b: str) -> str:
        # Invert both strings
        a, b = (a[::-1], b[::-1]) if len(a) >= len(b) else (b[::-1], a[::-1])

        ans, carry = "", 0
        for i in range(len(a)):
            # Convert each digit to integer
            x = ord(a[i]) - ord("0")
            y = ord(b[i]) - ord("0") if i < len(b) else 0

            # Update answer and carry digit
            ans = str((x + y + carry) % 2) + ans
            carry = (x + y + carry) // 2

        return "1" + ans if carry else ans
