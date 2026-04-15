from typing import List


class Solution:
    def closestTarget(self, words: List[str], target: str, start: int) -> int:
        # Base case
        if words[start] == target:
            return 0

        # Loop through the list and try to find the target string and calculate min dist
        n = len(words)
        i, ans = (start + 1) % n, float("inf")

        while i != start:
            if words[i] == target:
                ans = min(ans, abs(start - i), n - abs(start - i))
            i = (i + 1) % n

        return -1 if ans == float("inf") else ans
