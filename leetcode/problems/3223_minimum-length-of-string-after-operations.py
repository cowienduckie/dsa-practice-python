from typing import Counter


class Solution:
    def minimumLength(self, s: str) -> int:
        # Count the frequency of each character
        freq = [0] * 26
        for c in s:
            freq[ord(c) - ord("a")] += 1
        # If a letter has an odd frequency, we can minimize its length to 1
        # If a letter has an even frequency, we can minimize its length to 2
        ans = 0
        for f in freq:
            if f > 0:
                ans += 1 if f & 1 else 2
        return ans


class Solution:
    def minimumLength(self, s: str) -> int:
        return sum([1 if cnt & 1 else 2 for cnt in Counter(s).values()])
