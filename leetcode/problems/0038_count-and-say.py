class Solution:
    """
    Solution using recursion and run-length encoding (RLE).
    """

    def countAndSay(self, n: int) -> str:
        # Base case for recursion
        if n == 1:
            return "1"

        # Recursively get the previous RLE encoded string
        prev_encoded = self.countAndSay(n - 1) + "0"
        curr_digit = []
        encoded = []

        # Run-length encoding the previous string
        for i in range(len(prev_encoded)):
            if curr_digit and curr_digit[-1] != prev_encoded[i]:
                encoded.append(str(len(curr_digit)) + curr_digit[-1])
                curr_digit = []
            curr_digit.append(prev_encoded[i])

        # Join the encoded parts to form the final result
        return "".join(encoded)


class Solution:
    """
    Solution using iteration and run-length encoding (RLE).
    """

    def countAndSay(self, n: int) -> str:
        # Base case for iteration
        if n == 1:
            return "1"

        # Start with the first RLE encoded string
        prev_encoded = "1"

        # Iteratively build the RLE encoded string
        for _ in range(n - 1):
            prev_encoded += "0"
            curr_digit = []
            encoded = []

            # Run-length encoding the previous string
            for i in range(len(prev_encoded)):
                if curr_digit and curr_digit[-1] != prev_encoded[i]:
                    encoded.append(str(len(curr_digit)) + curr_digit[-1])
                    curr_digit = []
                curr_digit.append(prev_encoded[i])

            # Join the encoded parts to form the final result
            prev_encoded = "".join(encoded)

        return prev_encoded
