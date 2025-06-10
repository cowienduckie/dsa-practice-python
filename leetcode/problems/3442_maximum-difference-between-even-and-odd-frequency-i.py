class Solution:
    def maxDifference(self, s: str) -> int:
        freq = [0] * 26
        for c in s:
            freq[ord(c) - ord("a")] += 1

        max_odd = float("-inf")
        min_even = float("inf")
        for f in freq:
            if f == 0:
                continue
            elif f & 1:
                max_odd = max(max_odd, f)
            else:
                min_even = min(min_even, f)

        return max_odd - min_even
