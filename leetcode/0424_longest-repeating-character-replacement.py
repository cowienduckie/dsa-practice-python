from typing import Dict, List


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        char_dict: Dict[str, List[int]] = dict()
        char_dict[s[0]] = [0] * n
        char_dict[s[0]][0] = 1

        for i in range(1, n):
            if not s[i] in char_dict:
                char_dict[s[i]] = [0] * n
            for key, values in char_dict.items():
                values[i] = values[i - 1] + 1 if key == s[i] else values[i - 1]

        ans = 0
        for key, values in char_dict.items():
            l, r = 0, 0
            while r < n and l < n:
                steps = (r - l) - (values[r] - values[l]) + (0 if s[l] == key else 1)
                if steps <= k:
                    ans = max(ans, r - l + 1)
                    r += 1
                else:
                    l += 1
        return ans


class Solution2:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        # If k is large enough to replace all characters except one, return the length of the string
        if k >= n - 1:
            return n

        char_count = {}  # Dictionary to keep track of character frequencies
        max_count = 0  # Maximum frequency of a single character in the current window
        l = 0  # Left pointer of the sliding window
        max_length = 0  # Maximum length of the valid window

        # Iterate through the string with the right pointer
        for r in range(n):
            char_count[s[r]] = char_count.get(s[r], 0) + 1
            max_count = max(max_count, char_count[s[r]])

            # If the number of replacements needed exceeds k, shrink the window from the left
            while (r - l + 1) - max_count > k:
                char_count[s[l]] -= 1
                l += 1

            # Update the maximum length of the valid window
            max_length = max(max_length, r - l + 1)

        return max_length
