from typing import List, Set


class Solution:
    """
    Backtracking solution
    """

    def smallestNumber(self, pattern: str) -> str:
        # Add a dummy character to the end of the pattern
        pattern += "X"
        num = [0] * len(pattern)
        # Try to fill the first digit
        self.backtrack(0, num, set(), pattern)
        # Convert the numbers array to string
        return "".join([str(i) for i in num])

    def backtrack(self, i: int, num: List[int], used: Set[int], pattern: str) -> bool:
        # If we have filled all digits, return True
        if i == len(num):
            return True
        # Try to fill the current index with an unused digit
        for digit in range(1, 10):
            # Skip if the digit is already used or the pattern is not satisfied
            if (
                digit in used
                or (pattern[i - 1] == "I" and digit < num[i - 1])
                or (pattern[i - 1] == "D" and digit > num[i - 1])
            ):
                continue
            # Backtrack to fill the next digit
            used.add(digit)
            num[i] = digit
            if self.backtrack(i + 1, num, used, pattern):
                return True
            num[i] = 0
            used.remove(digit)
        # Return False if we cannot fill the current index
        return False
