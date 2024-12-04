class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        # Base cases
        if k == 1:
            return "0"
        elif k <= n:
            return "1"

        # Invert the string
        def invert(s: str) -> str:
            new_s = ""
            for i in range(len(s)):
                new_s += "1" if s[i] == "0" else "0"
            return new_s

        # Generate the string recursively
        def make_str(i: int, s: str) -> str:
            if i > n:
                return s
            return make_str(i + 1, s + "1" + invert(s)[::-1])

        return make_str(2, "0")[k - 1]
