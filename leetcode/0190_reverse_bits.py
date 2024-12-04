class Solution:
    """
    Follow up: If this function is called many times, how would you optimize it?
    Answer: Some possible solutions are
        - Store the computed results would be a good idea.
        - Pre-compute the results for all possible values and store them.
        - Use a divide and conquer approach, split the 32-bit number into groups of 8 bits (using byte and hexa), 4 bits, 2 bits, and 1 bit.
    """

    def reverseBits(self, n: int) -> int:
        ans = 0
        for i in range(32):
            ans = (ans << 1) + ((n >> i) & 1)
        return ans

    # def reverseBits(self, n: int) -> int:
    #     return int(f"{n:032b}"[::-1], 2)

    # def reverseBits(self, n: int) -> int:
    #     return int(bin(n)[2:].zfill(32)[::-1], 2)

    # def reverseBits(self, n: int) -> int:
    #     return int(format(n, '032b')[::-1], 2)
