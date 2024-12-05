class Solution:
    def getSum(self, a: int, b: int) -> int:
        # Define a mask to limit the size of the integers to 12 bits
        mask = 0xFFF

        # Loop until there is no carry
        while (b & mask) > 0:
            # Calculate the carry
            carry = (a & b) << 1

            # Sum without carry using XOR
            a = a ^ b

            # Update b with the carry
            b = carry

        # Return the result, ensuring it fits within 12 bits if there is still a carry
        return (a & mask) if b > 0 else a
