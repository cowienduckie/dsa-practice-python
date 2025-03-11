from collections import defaultdict


class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        # Use a dictionary to store occurrences of each letter
        memo = defaultdict(int)

        # Use sliding window to check every valid substring prefix
        ans = start = 0

        for end in range(len(s)):
            # Add the letter at end pointer
            memo[s[end]] += 1

            # If prefix substring [start..end] is valid, then every substring [start..end + X] is valid
            # So, try to shrink the window while the prefix substring is still valid
            while len(memo) == 3:
                # Update answer
                ans += len(s) - end

                # Remove the letter at start pointer
                memo[s[start]] -= 1
                if memo[s[start]] == 0:
                    memo.pop(s[start])

                # Increase start pointer
                start += 1

        return ans
