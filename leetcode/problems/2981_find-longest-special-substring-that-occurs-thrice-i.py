from collections import defaultdict


class Solution:
    """
    For each special substring with length k, we could see that:
        - Substring with length k occurs 1 time
        - Substring with length k - 1 occurs 2 times
        - Substring with length k - 2 occurs 3 times
    We have no need to care about the shorter substrings because they are definitely not the answer.

    So, we could traverse the string and check every consecutive substring with the same character.
    Store the frequency of top 3 longest special substrings for each character.
    """

    def maximumLength(self, s: str) -> int:
        stack = list(s)
        freq = [[0] * 51 for _ in range(26)]  # 50 is the maximum length of input string

        while stack:
            # Extract every special substring and their length
            letter = stack.pop()
            length = 1
            while stack and stack[-1] == letter:
                stack.pop()
                length += 1

            # Store the frequency of top 3 longest special substrings from above substring
            i = ord(letter) - ord("a")

            freq[i][length] += 1
            freq[i][length - 1] += 2 if length > 1 else 0
            freq[i][length - 2] += 3 if length > 2 else 0

        # Find the answer
        ans = -1
        for letter in range(26):
            for length in range(50, 0, -1):
                if freq[letter][length] >= 3:
                    ans = max(ans, length)
                    break

        return ans


class Solution:
    """
    Optimized version using dictionary to store the frequencies instead of pre-defined 2D array.
    """

    def maximumLength(self, s: str) -> int:
        stack = list(s)
        memo = defaultdict(lambda: defaultdict(int))

        while stack:
            # Extract every special substring and their length
            letter = stack.pop()
            length = 1
            while stack and stack[-1] == letter:
                stack.pop()
                length += 1

            # Store the frequency of top 3 longest special substrings from above substring
            memo[letter][length] += 1
            if length > 1:
                memo[letter][length - 1] += 2
            if length > 2:
                memo[letter][length - 2] += 3

        # Find the answer
        ans = -1
        for freq in memo.values():
            for k, v in freq.items():
                if v >= 3:
                    ans = max(ans, k)

        return ans
