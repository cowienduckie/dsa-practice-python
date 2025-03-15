from typing import List


class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        # Count the occurrences of each digit
        memo = [0] * 10
        for d in digits:
            memo[d] += 1

        # Start construct the numbers from the third digit
        return self._construct_numbers(memo, 3)

    def _construct_numbers(self, digits: List[int], place: int) -> int:
        # Base case
        if place == 0:
            return 1

        # Use backtracking to count valid numbers
        ans = 0
        for i in range(10):
            # No copies of this digit left
            if digits[i] == 0:
                continue

            # If the current is 3rd digit, only take the even and 0
            if place == 3 and i % 2 == 1:
                continue

            # If the current is 1st digit, take every digit except 0
            if place == 1 and i == 0:
                continue

            # Backtracking
            digits[i] -= 1
            ans += self._construct_numbers(digits, place - 1)
            digits[i] += 1

        return ans
