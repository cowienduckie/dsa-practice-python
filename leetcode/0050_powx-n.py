class Solution:
    def myPow(self, x: float, n: int) -> float:
        # Exponent is 0
        if n == 0:
            return 1

        # Exponent is negative
        if n < 0:
            return 1 / self.myPow(x, n * -1)

        # Exponent is odd
        if n % 2 == 1:
            return self.myPow(x, n - 1) * x

        # Exponent is even
        square_root = self.myPow(x, n / 2)

        return square_root * square_root
