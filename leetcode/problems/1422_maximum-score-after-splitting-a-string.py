class Solution:
    def maxScore(self, s: str) -> int:
        n = len(s)
        # Store prefix number of 0s on the left of i (not including i)
        prefix = [0] * n
        for i in range(1, n):
            prefix[i] = prefix[i - 1] + (1 if s[i - 1] == "0" else 0)

        # Store suffix number of 1s on the right of i (including i)
        suffix = [0] * n
        suffix[n - 1] = 1 if s[n - 1] == "1" else 0
        for i in range(n - 2, -1, -1):
            suffix[i] = suffix[i + 1] + (1 if s[i] == "1" else 0)

        # Find the max score when break the string at the start index i of right substring
        ans = 0
        for i in range(1, n):
            ans = max(ans, prefix[i] + suffix[i])
        return ans
