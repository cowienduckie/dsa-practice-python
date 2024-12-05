class Solution:
    def minEnd(self, n: int, x: int) -> int:
        """
        If we want AND of all elements of the array to be X (E.g. 1100101), we start the array with X.
        Then, we try to fill the array with numbers sharing the same 1-bits as X.

        We call
            - A is the total bits of X.
            - B is the number of 0-bits in X.

        So
            - By filling the 0-bits of X with all possible combinations of 0 and 1, we can get 2**B different numbers.
            - By adding 2**A to X, we can get the next number that shares the same A rightmost bits as X to perform the above operation again.
        """
        # Convert x to binary string and get its length
        bit_str = bin(x)[2:]
        bit_len = len(bit_str)

        # Find positions of '0' bits in x
        zero_positions = []
        for i in range(bit_len):
            if bit_str[bit_len - i - 1] == "0":
                zero_positions.append(i)
        zero_count = len(zero_positions)

        # Adjust x and n if n is greater than or equal to 2^zero_count
        if n >= 2**zero_count:
            x += (n // 2**zero_count) * 2**bit_len
            n %= 2**zero_count

        # If n is zero, adjust N and X to perform the filling 0-bits operation
        if n == 0:
            n = 2**zero_count
            x -= 2**bit_len

        # X is already the first combination so we start from the next one
        # N's binary string is now the final combination we need to fill
        n -= 1

        # Try to fill the 0-bits of X with binary string of n
        for pos in zero_positions:
            if n & 1:
                x += 2**pos
            n >>= 1

        return x
